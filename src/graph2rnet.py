#!/usr/bin/env python3

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description="Convert graph to rnet format")
    parser.add_argument("node_file")
    parser.add_argument("edge_file")
    parser.add_argument("-o", "--out", metavar="OUTPUT", help="output dest (default: a.rnet)", default="a.rnet")
    parser.add_argument("-s", "--sep", help="input file separator (default: space)", default=' ')
    parser.add_argument("-n", metavar="NODE_ID_COL", help="col node_id in node_file (default: 1)", type=int, default=1)
    parser.add_argument("-l", metavar="NODE_LNG_COL", help="col node_lng in node_file (default: 2)", type=int, default=2)
    parser.add_argument("-k", metavar="NODE_LAT_COL", help="col node_lat in node_file (default: 3)", type=int, default=3)
    parser.add_argument("-r", "--row", help="set if edge_file has header row (default: unset)", action="store_true")
    parser.add_argument("-f", metavar="EDGE_FROM_COL", help="col from_id in edge_file (default: 1)", type=int, default=1)
    parser.add_argument("-t", metavar="EDGE_TO_COL", help="col to_id in edge_file (default: 2)", type=int, default=2)
    return parser


def graph2rnet(args):
    nodes = {}
    edges = {}
    edge_id = 0

    with open(args["node_file"], 'r') as f_node_file:
        for line in f_node_file:
            cols = line.split(args["sep"])
            nodes[int(cols[args['n']-1])] = [float(cols[args['l']-1]), float(cols[args['k']-1])]

    with open(args["edge_file"], 'r') as f_edge_file:
        if args["row"]:
            f_edge_file.readline()
        for line in f_edge_file:
            cols = line.split(args["sep"])
            edges[edge_id] = [int(cols[args['f']-1]), int(cols[args['t']-1])]
            edge_id+=1

    with open(args["out"], 'w') as f_out:
        for edge_id, edge in edges.items():
            from_id = edge[0];
            from_lng = str(nodes[from_id][0])
            from_lat = str(nodes[from_id][1])
            to_id = edge[1];
            to_lng = str(nodes[to_id][0])
            to_lat = str(nodes[to_id][1])
            row = "{} {} {} {} {} {} {}\n".format(edge_id, from_id, to_id,
                    from_lng, from_lat, to_lng, to_lat)
            f_out.write(row)


if __name__ == "__main__":
    parser = get_parser()
    args = vars(parser.parse_args())
    graph2rnet(args)
