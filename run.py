import os
import sys
import subprocess

# Use Render's PORT
port = os.environ.get('PORT', '8000')
cmd = ['mcp-neo4j-cypher', '--transport', 'sse', '--server-host', '0.0.0.0', '--server-port', port, '--server-path', '/sse']
subprocess.run(cmd)
