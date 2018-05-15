try:
    ...
except Exception as e:
    ...
    log('Reason:', e)  # Important!

# SystemExit KeyboardInterrupt GeneratorExit
# Use BaseException
