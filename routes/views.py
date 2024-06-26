from django.shortcuts import render
import json
from py2neo import Graph
import csv
#!flask/bin/python
from py2neo import Graph
import json
from collections import defaultdict
import heapq
import sys,jsonify
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt



# Create your views here.





# # import relationships
# with open('C:/Users/user/Desktop/Aerothon/aerodirection/data/flights_83.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
    
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#         line_count += 1
#         print(row['ORIGIN_AIRPORT'], row['DESTINATION_AIRPORT'], row['DISTANCE'])
#         print(graph.run("match (a:Airports), (b:Airports) where a.IATA_CODE = '"+row['ORIGIN_AIRPORT']+"' and b.IATA_CODE = '"+row['DESTINATION_AIRPORT']+"' merge (a)-[r:airline{distance: "+row['DISTANCE']+"}]-(b)"))
# print(line_count)






# graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))
# # tx = graph.begin()
# print(graph.run("MATCH (a:Airports) WHERE a.STATE = 'TX' RETURN a").to_table())
# print(graph.evaluate("MATCH (a:Airports) WHERE a.STATE = 'TX' RETURN count(a)"))

# with open('C:/Users/user/Desktop/Aerothon/aerodirection/data/flights_83.csv', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
    
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#         line_count += 1
#         print(row['ORIGIN_AIRPORT'], row['DESTINATION_AIRPORT'], row['DISTANCE'])
#         print(graph.run("match (a:Airports), (b:Airports) where a.IATA_CODE = '"+row['ORIGIN_AIRPORT']+"' and b.IATA_CODE = '"+row['DESTINATION_AIRPORT']+"' create (a)-[r:airline{distance: "+row['DISTANCE']+"}]->(b)"))
#     print(line_count)
    


class Network:
    def __init__(self):
        self.vertices = {}
 
    def add_vertex(self, name, edges):
        self.vertices[name] = edges
 
    def get_shortest_path(self, startpoint, endpoint):
        distances = {}
        previous = {}
        nodes = []
 
        for vertex in self.vertices:
            if vertex == startpoint:
                
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            elif vertex in self.vertices[startpoint]:
                
                distances[vertex] = self.vertices[startpoint][vertex]
                heapq.heappush(nodes, [self.vertices[startpoint][vertex], vertex])
                previous[vertex] = startpoint
            else:
                distances[vertex] = sys.maxsize
                heapq.heappush(nodes, [sys.maxsize, vertex])
                previous[vertex] = None
 
        while nodes:
            smallest = heapq.heappop(nodes)[1]
            if smallest == endpoint:
                shortest_path = []
                lenPath = distances[smallest]
                temp = smallest
                while temp != startpoint:
                    shortest_path.append(temp)
                    temp = previous[temp]
               
                shortest_path.append(temp)
            if distances[smallest] == sys.maxsize:
                
                break
            
            for neighbor in self.vertices[smallest]:
                dis = distances[smallest] + self.vertices[smallest][neighbor]
                if dis < distances[neighbor]:
                    distances[neighbor] = dis
                    
                    previous[neighbor] = smallest
                    for node in nodes:
                        if node[1] == neighbor:
                            
                            node[0] = dis
                            break
                    heapq.heapify(nodes)
        return distances, shortest_path, lenPath
 
    def getMinDistancesIncrement(self, inputList):
        inputList.sort()
        lenList = [v[0] for v in inputList]
        minValue = min(lenList)
        minValue_index = lenList.index(minValue)
        minPath = [v[1] for v in inputList][minValue_index]
        return minValue, minPath, minValue_index
 
 
    def k_shortest_paths(self,start, finish, k = 3):

        distances, _, shortestPathLen = self.get_shortest_path(start, finish)
        num_shortest_path = 0
        paths = dict()
        distancesIncrementList = [[0, finish]]
        while num_shortest_path < k:
            path = []

            minValue, minPath, minIndex = self.getMinDistancesIncrement(distancesIncrementList)
            smallest_vertex = minPath[-3:]
            distancesIncrementList.pop(minIndex)
 
            if smallest_vertex == start:
                path.append(minPath[::-1])
                num_shortest_path += 1

                paths[path[0]] = minValue + shortestPathLen

                continue
 
            for neighbor in self.vertices[smallest_vertex]:
                incrementValue = minPath
                increment = 0
                if neighbor == finish:
                    
                    continue
                if distances[smallest_vertex] == (distances[neighbor] + self.vertices[smallest_vertex][neighbor]):
                    increment = minValue
                elif distances[smallest_vertex] < (distances[neighbor] + self.vertices[smallest_vertex][neighbor]):
                    increment = minValue + distances[neighbor] + self.vertices[smallest_vertex][neighbor] - distances[smallest_vertex]
                elif distances[neighbor] == (distances[smallest_vertex] + self.vertices[smallest_vertex][neighbor]):
                    increment = minValue + 2 * self.vertices[smallest_vertex][neighbor]
                distancesIncrementList.append([increment, incrementValue + neighbor])
        return paths
    




def request1(start,end):
    # create network
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))
    rel = graph.run("MATCH (a:Airports)-[r]-(b:Airports) RETURN a.IATA_CODE, b.IATA_CODE, r.distance").to_table()

    g = Network()
    vsets = {}
    for edge in rel:
        if edge[0] not in vsets:
            vsets[edge[0]] = {edge[1]: edge[2]}
        else:
            vsets[edge[0]].update({edge[1]: edge[2]})
            
        if edge[1] not in vsets:
            vsets[edge[1]] = {edge[0]: edge[2]}
        else:
            vsets[edge[1]].update({edge[0]: edge[2]})
    for key, value in vsets.items():
        g.add_vertex(key, value)
    


    k = 3
    distances, shortestPath, shortestPathLen = g.get_shortest_path(start, end)
    paths = g.k_shortest_paths(start, end, k)
    res = []
    for path, length in paths.items():
        temp = []
        for i in range(0, len(path),3):
            temp.append(path[i+2]+path[i+1]+path[i])
        res.append(temp)
    # print(res)

    response, data = {}, []
    for i in res:
        airports = i
        arr = []
        for airport in airports:
            details = graph.run("MATCH (n:Airports) WHERE n.IATA_CODE = '" +airport+"' RETURN n.STATE, n.AIRPORT, n.CITY, n.LATITUDE, n.LONGITUDE, n.IATA_CODE").to_table()
        # convert table into json
            n = details[0]
            temp = {'state': n[0], 'airport': n[1], 'city': n[2], 'latitude': n[3], 'longitude': n[4], 'code':n[5]}
            arr.append(temp)
        data.append(arr)
    response['data'] = data


    return response 


@csrf_exempt
def home(request):
    


   # template = loader.get_template('index.html')
    return render(request, 'index.html')


@csrf_exempt
def rout(request):
    cotext={}  
    if request.method == 'POST':
        Source = request.POST.get('Source')
        distination = request.POST.get('distination')
        if Source =='' or distination=='':
            return render(request, 'error.html')

        data=request1( Source ,distination)
        airport_codes_list = [[entry['code'] for entry in sublist] for sublist in data['data']]
     
        for i, codes in enumerate(airport_codes_list):
          print(f"List {i + 1}: {codes}")
          cotext[f"ROUTE {i + 1}"]=codes
    print(cotext)


    return render(request, 'index.html',{'json_data': cotext})

