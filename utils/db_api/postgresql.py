import os
from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from dotenv.main import load_dotenv

load_dotenv()

NAME = os.getenv('DB_NAME')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')


class Database:
    def __init__(self) -> None:
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=USER,
            password=PASSWORD,
            host=HOST,
            database=NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_products(self):
        sql = """
        CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price INT NOT NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    async def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = '{parameters[item]}'" for num, item in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    @staticmethod
    async def format_args_select(sql: str, *args):
        sql += ' '
        if '*' in args or not args:
            return sql + ' * '
        sql += " , ".join([
            f"{item}" for item in args
        ])
        return sql

    @staticmethod
    async def format_args_insert(sql: str, all, *args, **kwargs):
        if all:
            sql += '(' + " , ".join([
                f"{key}" for key in kwargs.keys()
            ]) + ')'
            args = kwargs.values()
        sql += ' values (' + " , ".join([
            f"{item}" for item in args
        ]) + ')'

        return sql

    async def add_product(self, table: str, all=False, **kwargs):
        sql = f"INSERT INTO {table}"
        sql = self.format_args_insert(sql, all, **kwargs)
        return await self.execute(sql, fetchrow=True)

    async def select_all_from_table(self, table, *args, **kwargs):
        sql = await self.format_args_select('select', *args)
        sql += f" from {table}"
        if kwargs.keys():
            sql += ' where '
        sql, parameters = await self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, fetch=True)

    async def select_detail_from_table(self, table: str, *args, **kwargs):
        sql = await self.format_args_select('select', *args)
        sql += f" from {table}"
        if kwargs.keys():
            sql += ' where '
        sql, parameters = await self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, fetchrow=True)

    async def delete(self, table: str, **kwargs):
        sql = f'DELETE FROM {table}'
        if not kwargs.keys():
            sql+=' WHERE TRUE'
        sql = await self.format_args(sql, **kwargs)
        await self.execute(sql, execute=True)

    async def drop_database(self, database: str):
        await self.execute(f"DROP DATABASE {database}", execute=True)
