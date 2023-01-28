from helpers.numeral_ref import NumeralRefPage as r
from helpers.excel_ref import ExcelRef as e

def test_ref(browser_page):
    assert r(browser_page).numeral_ref(4) == 'IV'

def test_excel():
    assert e.extract_cell_classic(4) == 'IV'
    assert e.extract_cell_simplified(4) == 'IV'

def excel(num):
    return e.extract_cell_simplified(num)

def test_online_and_excel(browser_page):
    assert r(browser_page).numeral_ref(399) == e.extract_cell_classic(399)

def numbers_list(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)
    return num_list

from approvaltests.combination_approvals import verify_all_combinations

def test_all_on_excel():
    verify_all_combinations(excel, [
        numbers_list(100)])

def test_all_on_browser(browser_page):
    verify_all_combinations(r(browser_page).numeral_ref, [
        numbers_list(100)])



# Developer intent, part 0. Review for correctness and consiceness

# Developer intent, part 1. Input -> Output
# Developer intent, part 2. Rules of behavior boundaries
# Developer intent, part 3. Coverage (pytest --cov=important_program important_program.py)
# Developer intent, part 4. Sampling vs wide nets (approvals)
# Developer intent, part 5. Properties

# Domain, laymen. Why oh why this?
# Domain, laymen. Rules. More rules.

# Domain, expert. Why oh why this?
# Domain, expert. Real and real boundaries.

# References. Give me the answers!
# References. Answers aren't as simple as you think.

# User filtering. No user would do what users would do.