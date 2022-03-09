//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStor {
    uint256 favoriteNumber;

    // This is a comment!
    struct People1 {
        uint256 favoriteNumber1;
        string name;
    }

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber + favoriteNumber;
    }

    People1[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People1(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
