# JsonScript
modern database :)

A modern database based on sql

### Purpose
Learning multiple ways to use databases is annoying and a waste of time

The aim of JsonScript is to imitate the ways of sql but for json as sql is easier to understand in .sql files

This is because it looks something like this

```sql
SELECT x
USE example;
```

Meanwhile JsonScript

```
SELECT hello
USE example
```

Selecting multiple
```
SELECT hello, hi 
SELECT hola,hey
USE example
```

If the value is not just one away

eg.

the json:
```json
{"hello":{"hi":"I need hi","bye":"don't need this"}}
```
the JsonScript:
```
SELECT hello:hi
USE example
SHOW
```
output:
```json
{"hello":{"hi":"I need hi"}}
```


To show the database in json simply add

```
SELECT hello
USE example
SHOW
```

To create a database:

```
CREATE example
```
If the file already exists it will be ignored

To delete a database:

```
DELETE example
```
If the file doesn't exists it passes over

To insert values:

json:
```json
{}
```

JsonScript:
```
USE example
INSERT this:is AS an example
SHOW example
```

Output:
```json
{"this":{"is":"an example"}}
```

Leave blank for the most previously defined USE to show

### TODO :
[-] SELECT, USE and SHOW

[-] INSERT

[ ] GET
