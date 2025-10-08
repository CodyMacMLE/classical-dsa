# Personal Implementation of Classical Data Structures and Algorithms
My own implementation of all the classical data structures and algorithms explained in BTP500 (DSA)

## Scripts
#### run everything (pytest + lint)
```tox```

#### just tests
```tox -e pytests```

#### just linter
```tox -e lint```

#### pass args through to pytest (everything after -- goes to pytest)
```tox -e pytests -- -k "my_test_name" tests/unit/test_something.py```
