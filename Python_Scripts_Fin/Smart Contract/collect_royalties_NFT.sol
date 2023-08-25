pragma solidity ^0.8.0;

contract NFT {
    mapping (bytes32 => address) public tokenIdToOwner;
    mapping (bytes32 => uint256) public tokenIdToRoyalties;
    mapping (bytes32 => bytes) public tokenIdToAudioSample;
    address payable public royaltiesCollector;

    event Transfer(bytes32 indexed tokenId, address indexed from, address indexed to);
    event RoyaltiesCollected(bytes32 indexed tokenId, uint256 royalties);
    event AudioSampleUploaded(bytes32 indexed tokenId, bytes sample);

constructor() public payable {
    roles[msg.sender] = true;
    royaltiesCollector = msg.sender; //payab addy here 
}

mapping (address => bool) public roles;
bool public paused = false;

modifier onlyWhenNotPaused() {
    require(!paused, "contract is paused");
    _;
}

constructor() public {
    roles[msg.sender] = true;
    royaltiesCollector = msg.sender;
}

function pause() public {
    require(roles[msg.sender], "only admin can pause the contract");
    paused = true;
}

function unPause() public {
    require(roles[msg.sender], "only admin can unpause the contract");
    paused = false;
}

function mint(address owner, bytes32 tokenId, uint256 royalties, bytes memory sample) public onlyWhenNotPaused {
    require(tokenIdToOwner[tokenId] == address(0), "Token ID already in use");
    tokenIdToOwner[tokenId] = owner;
    tokenIdToRoyalties[tokenId] = royalties;
    tokenIdToAudioSample[tokenId] = sample;
    emit Transfer(tokenId, address(0), owner);
    emit AudioSampleUploaded(tokenId, sample);
}

function transfer(bytes32 tokenId, address to) public onlyWhenNotPaused {
    require(tokenIdToOwner[tokenId] == msg.sender, "Only the owner can transfer the NFT");
    address previousOwner = tokenIdToOwner[tokenId];
    tokenIdToOwner[tokenId] = to;
    emit Transfer(tokenId, previousOwner, to);
}

function collectRoyalties(bytes32 tokenId) public onlyWhenNotPaused {
    require(tokenIdToOwner[tokenId] == msg.sender, "Only the owner can collect royalties for the NFT");
    uint256 royalties = tokenIdToRoyalties[tokenId];
    royaltiesCollector.transfer(royalties);
    emit RoyaltiesCollected(tokenId, royalties);
}

    function updateRoyalties(bytes32 tokenId, uint256 newRoyalties) public {
    require(tokenIdToOwner[tokenId] == royaltiesCollector, "Only the royalties collector can update royalties");
    tokenIdToRoyalties[tokenId] = newRoyalties;
}

}
