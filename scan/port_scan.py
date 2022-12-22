import scanless
s1 = scanless.Scanless()
output = s1.scan("103.42.31.67")
print(output['raw'])

import json
# print(json.dumps(output['parsed']))