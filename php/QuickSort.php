<?php

function partition(&$sortArray, $low, $high) {
	$index = $low-1;
	$pivot = $sortArray[$high];

	for($j=$low; $j<$high; $j++) {
		if($sortArray[$j] <= $pivot) {
			$index = $index + 1;
			$temp = $sortArray[$j];
			$sortArray[$j] = $sortArray[$index];
			$sortArray[$index] = $temp;
		}
	}

	$index = $index + 1;
	$temp = $sortArray[$index];
	$sortArray[$index] = $sortArray[$high];
	$sortArray[$high] = $temp;
    return $index;
}

function quickSort(&$sortArray, $low, $high) {
	if ($low < $high) {
		$pIndex = partition($sortArray, $low, $high);
		quickSort($sortArray, $low, $pIndex-1);
		quickSort($sortArray, $pIndex+1, $high);
	}
}

$sortArray = array(10, 7, 8, 9, 1 ,5);
quickSort($sortArray, 0, count($sortArray)-1);

foreach($sortArray as $ele) {
    echo $ele.' ';
}


?>