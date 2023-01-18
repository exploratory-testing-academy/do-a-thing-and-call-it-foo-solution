# Do a Thing and Call It Foo -Solution

@maaretp runs a testing talk/workshop with title 'Let's Do a Thing and Call It Foo' that is set up around exploratory unit testing of roman numerals converter. This project is the solution sample.

The exercise covers a checklist of steps:

* Developer intent, part 0. Review for correctness and consiceness
* Developer intent, part 1. Input -> Output
* Developer intent, part 2. Rules of behavior boundaries
* Developer intent, part 3. Coverage (pytest --cov=important_program important_program.py)
* Developer intent, part 4. Sampling vs wide nets (approvals)
* Domain, laymen. Why oh why this?
* Domain, laymen. Rules. More rules.
* Domain, expert. Why oh why this?
* Domain, expert. Real and real boundaries.
* References. Give me the answers!
* References. Answers aren't as simple as you think.
* User filtering. No user would do what users would do.

The general facilitation of the exercise runs in a few sections:

* With GitHub Copilot as our programmer and us all as its testers, choose our solution suggested from describing intent as code comment (e.g. #Converts numbers to roman numerals)
* First tests, both positive (input gives roman numeral) and negative (input gives error message), and scale to parametrized tests
* Reference implementations, both browser and excel
* From handpicked values to generating values
* Realizing we were on the wrong domain rules

Due to **exploratory** nature of the exercise, facilitator should follow the group's order in which they discover information. Most of the time the exercise is run keeping the checklist hidden, but with most recent rounds of teaching new people on testing, having checklist available helps modeling the tester intent exploratory testers usually hold inside their heads on a small, specific problem.

## Instructions

## Set up

```bash
#!/bin/bash
python -m venv .venv
pip install -r requirements.txt
playwright install
```

VSCode extensions:

* (optional) Coverage Gutters
* (optional, paid service) GitHub Copilot

### Run tests

```bash
#!/bin/bash
pytest important_program.py
```

### Run tests under coverage

```bash
#!/bin/bash
pytest --cov=important_program important_program.py
```

### For starting approvaltests with a good reporter

```bash
#!/bin/bash
pytest --approvaltests-use-reporter='PythonNative'
```
