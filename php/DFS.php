<?php

class Graph {

	public $graph = array();

	public $visited = array();

	public function __construct($graph){
		$this->graph = $graph;
	}

 	public function DFS($node) {
	 	array_push($this->visited, $node);
	 	echo $node;
	 	foreach($this->graph[$node] as $key => $value) {
	 		if($value == 1 && !in_array($key, $this->visited)) {
	 			$this->DFS($key);
	 		}
 		}
 	}

}

$graph = array(
	      array(0,1,1,1,0,0,1),
	      array(1,0,1,0,0,0,0),
	      array(1,1,0,0,1,0,0),
	      array(1,0,0,0,0,1,0),
	      array(0,0,1,0,0,1,0),
	      array(0,0,0,1,1,0,1),
	      array(1,0,0,0,0,1,0),
	   );
$g = new Graph($graph);
$g->DFS(0);

?>