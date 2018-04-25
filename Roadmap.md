# Idea Roadmap



## Features

* Support for Processes and Pools
  * Synchronous and Asynchronous
  * Output Handling
* Logging
  * Yes, even from the processes/pools
* Plugin Support
  * Web UIs
  * GUIs
  * APIS
  * GPU Processing
  * And so much more...



## Commands

* Main Commands
  * Initial import: `import spasm`
* Process/Pool Commands
  * Starting a Process: `process = spasm.Process()`
  * Starting a Pool: `pool = spasm.Pool()`
  * Start
  *  Attributes:
    * name - Name of the process (Process only)
    * timeout - default timeout
    * init - custom initialize function
    * async - set to true for default asynchronous processing
    * cpus - Number of processes to make in pool (Pool only)
  * Methods:
    * run() - Runs the given function
      * timeout - timeout of this function, default=None
    * stop() - Stops the function gracefully
    * kill() - Stops the function ungracefully
  * Getting Returns
    * `results = process.run(function, (args,))`
    * `results = pool.run(function, (args,))`
* Logging
* Plugins

