import aiosqlite

async def getdb():
  return await aiosqlite.connect("count.db")

async def table():
  conn = await getdb()
  cur = await conn.cursor()
  await cur.execute("CREATE TABLE IF NOT EXISTS count (count INTEGER DEFAULT 0)")
  await conn.commit()
  await conn.close()

async def getCount():
  conn = await getdb()
  cur = await conn.cursor()
  await cur.execute("SELECT count FROM count")
  count = await cur.fetchone()
  await conn.close()
  return count[0]

async def addCount():
  conn = await getdb()
  cur = await conn.cursor()
  await cur.execute("SELECT count FROM count")
  data = await cur.fetchone()
  if data:
    await cur.execute("UPDATE count SET count = count + 1")
  else:
    await cur.execute("INSERT INTO count (count) VALUES (1)")
  await conn.commit()
  await conn.close()