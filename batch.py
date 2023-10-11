from netpyne import specs
from netpyne.batch import Batch

def runBatch():
        # Create variable of type ordered dictionary
        params = specs.ODict()

        #fill in with parameters to explore a range of values
        params = {'amp': [0.3, 0.4, 0.5, 0.6]}

        #create Batch object with parameters to modify and specify files to use
        b = Batch(params = params, cfgFile = 'cfg.py', netParamsFile = 'netParams.py')

        #Set output folder, grid method and run configuration
        b.batchLabel = 'amp'
        b.saveFolder = 'nbatch_traces_-TF'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin', 'script': 'init.py', 'skip': True}

        #run batch simulations
        b.run()

#Main code
if __name__ == '__main__':
        runBatch()

#params = {'amp': [ ]}

#grid = Batch()

#grid.runCfg = {}
    
#grid.run()

#cfg.amp = 0.2

#hh.set_mappings('cfg')