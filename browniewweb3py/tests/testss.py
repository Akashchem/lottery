from brownie import SimpleStor, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStor.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStor.deploy({"from": account})
    # Act
    expected = 15
    txn = simple_storage.store(expected, {"from": account})
    txn.wait(1)
    # Assert
    assert expected * 2 == simple_storage.retrieve()
