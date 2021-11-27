# MDB
modern database :)

A modern database based on sql

### Purpose
Learning multiple ways to use databases is annoying and a waste of time

The aim of MDB is to imitate the ways of sql but for json as sql is easier to understand in .sql files

This is because it looks something like this

```sql
SELECT x
FROM example;
```

Meanwhile MDB

```
SELECT hello
FROM example
```

Selecting multiple
```
SELECT hello, hi 
SELECT hola,hey
FROM example
```

If the value is not just one away

eg.

the json:
```json
{"hello":{"hi":"I need hi","bye":"don't need this"}}
```
the mdb:
```
SELECT hello:hi
FROM example
SHOW
```
output:
```json
{"hello":{"hi":"I need hi"}}
```


To show the database in json simply add

```
SELECT hello
FROM example
SHOW
```

Leave blank for the most previously defined FROM to show

### TODO :
[-] SELECT, FROM and SHOW

[ ] INSERT

[ ] GET
