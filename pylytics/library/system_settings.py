# For now the batch size is hardcoded (i.e. the number of rows inserted per
# insert statement). Eventually this will be dynamically sized based on the
# max packet size.
BATCH_SIZE = 1000

# If this is set, all available cores will be used during CPU bound operations.
ENABLE_MP = True
