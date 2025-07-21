import os
import sys
import subprocess

# Use Render's PORT
port = os.environ.get('PORT', '8000')
cmd = ['mcp-neo4j-cypher', '--transport', 'sse', '--host', '0.0.0.0', '--port', port]
subprocess.run(cmd)
