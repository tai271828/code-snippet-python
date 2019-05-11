# Build the Development Environment

```
pipenv install
pipenv shell
```

# Run the Example

```
./run.py start
```

and then monitor the expected output

```
tail -f sleepy.log
```

Stop it by

```
./run.py stop
```

You should see the stopping message in the output log as well.
