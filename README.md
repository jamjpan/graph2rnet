###graph2rnet

Convert graph (node, edge files) into an "rnet" file.

The rnet (road-network) file format is space separated columns, looks like this:
```
edge_id from_id to_id from_lng from_lat to_lng to_lat
```

The `edge_id` is automatically generated.

Why? Because sometimes graphs come in node/edge files, that is difficult to
plot, but with the rnet file, it is very easy to plot. Example using gnuplot:
```
plot 'output.rnet' using 4:5:($6-$4):($7-$5) w vectors nohead lt rgb 'black' lw 1
```

Node file should contain node id, latitude, and longitude columns for each node.
Edge file should contain the id of the from and to nodes for each edge.
Edge file is allowed to have a header. Use -r to tell graph2rnet to skip the
header row.

The columns format and column separator can be specified in the options.

Check graph2rnet -h for usage.

Example:
```
node_file.dat
    0 72.433 33.983
    1 72.412 33.783
    ...
edge_file.dat (has header, and 3rd col is weight (ignored))
    12 10
    0 1 7
    0 2 3
    ...

graph2rnet node_file.dat edge_file.dat -r -o "output.rnet"

0 0 1 72.433 33.983 72.412 33.783
...
```
