<?php

$graph = array(
      array(0,1,1,1,0,0,1),
      array(1,0,1,0,0,0,0),
      array(1,1,0,0,1,0,0),
      array(1,0,0,0,0,1,0),
      array(0,0,1,0,0,1,0),
      array(0,0,0,1,1,0,1),
      array(1,0,0,0,0,1,0),
   );

$queue = array(0);
$visited = array(0);

while(count($queue) > 0) {
  $node = array_pop($queue);
  foreach($graph[$node] as $key => $value){
      if($value == 1 && !in_array($key, $visited)) {
          array_push($visited, $key);
          array_unshift($queue, $key);
      }
  }
}

foreach($visited as $nodeVisit) {
  echo $nodeVisit."<br/>";
}

?>