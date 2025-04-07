from app import app
from flask import render_template, request, jsonify
import networkx as nx

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el archivo index.html

# Ruta para ejecutar el algoritmo de Dijkstra
@app.route('/dijkstra', methods=['POST'])
def dijkstra():
    try:
        # Obtener datos del formulario
        data = request.json  # Supone que los datos llegan en formato JSON
        nodes = data['nodes']
        edges = data['edges']
        start = data['start']
        end = data['end']

        # Crear el grafo
        G = nx.DiGraph()  # Grafo dirigido
        for node in nodes:
            G.add_node(node)

        for edge in edges:
            # Suponemos que cada 'edge' es una lista [nodo1, nodo2, peso]
            if len(edge) == 3:
                G.add_edge(edge[0], edge[1], weight=edge[2])
            else:
                return jsonify({'error': 'Edge is missing weight or has incorrect format'}), 400

        # Ejecutar el algoritmo de Dijkstra
        try:
            shortest_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
            path_length = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')
            return jsonify({
                'shortest_path': shortest_path,
                'path_length': path_length
            })
        except nx.NetworkXNoPath:
            return jsonify({'error': 'No path found between the nodes'}), 404
    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500
