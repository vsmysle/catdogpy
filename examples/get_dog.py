"""Example of the Dog API usage."""
from catdog import Dog

'''
NOTHING HERE YET

Later, all of this will be done as a tests (inside tests/ directory).
'''
# just testing stuff, WIP
dog = Dog('MY_TEST_KEY')
dog.get_by_id(1)
dog.delete(1)

# dog delete should not work without api_key
dog.api_key = None
dog.get_by_id(2)

# should raise an exception
dog.delete(2)
