<?php

function binarySearch($arr, $l, $r, $target) {
	if($r >= 1 && $r >= $l) {
		$mid = floor($l + ($r - $l)/2);

		if ($arr[$mid] == $target) {
			return $mid;
		} else if($arr[$mid] < $target) {
			return binarySearch($arr, $mid+1, $r, $target);
		} else {
			return binarySearch($arr, $l, $mid-1, $target);
		}

	} else {
		return false;
	}

}

$arr = array(2, 3, 4, 10, 40);
$x = 40;

$result = binarySearch($arr, 0, count($arr) - 1, $x);
if($result) {
	echo $result;
} else {
	echo 'invalid';
}

?>