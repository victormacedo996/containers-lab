from asyncpg import Pool

class EmployeeRepository:

    def __init__(self, pool: Pool) -> None:
        self.pool = pool

    async def get_employee(self, employee_id: int) -> dict:

        query = "SELECT * FROM employees WHERE id = $1"
        async with self.pool.acquire() as conn:
            result = await conn.fetch(query, employee_id)

        if result:
            return [dict(result) for result in result][0]
        
        return None
            