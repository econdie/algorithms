<?php 

class Node {

	public $val = null;
	public $left = null;
	public $right = null;

	public function __construct($val){
		$this->val = $val;
	}
}

function searchTree($root, $key) {
	if($root == null || $root->val == $key) {
		return $root;
	} else if($root->val < $key) {
		return searchTree($root->right, $key);
	} else {
		return searchTree($root->left, $key);
	}
}

function insertNode($root, $node) {
	if($root == null) {
		$root = $node;
	} else {
		if($root->val < $node->val) {
			if($root->right == null) {
				$root->right = $node;
			} else {
				insertNode($root->right, $node);
			}
		} else {
			if($root->left == null) {
				$root->left = $node;
			} else {
				insertNode($root->left, $node);
			}
		}
	}
}

$nodeA = new Node(5);
$nodeB = new Node(8);
$nodeC = new Node(11);
$nodeD = new Node(15);
$nodeE = new Node(4);

$nodeA->left = $nodeE;
$nodeA->right = $nodeC;
$nodeC->left = $nodeB;
$nodeC->right = $nodeD;

$result = searchTree($nodeA, 11);
if($result == null) {
    echo 'no results';
} else {
    echo $result->val.' ';
}

$newNode = new Node(17);
insertNode($nodeA, $newNode);
echo $nodeD->right->val;

?>