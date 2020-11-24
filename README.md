---


---

<h1 id="pypliner-data-processor">Pypliner-data-processor</h1>
<p>The aim of this project is to allow a great modularity in the development of data processes based on the execution sequence of scripts.</p>
<p>The original idea was to provide a central script that would receive as input a configuration file, from which it would be able to import and execute the different scripts.</p>
<p>The power of this tool lies in the fact that it allows to inject the result of a given script to a target script as a parameter. All this based only on the simple configuration file (JSON).</p>
<h2 id="install">Install</h2>
<p>First clone this repository</p>
<pre><code>git clone https://github.com/yossefaz/pypliner-data-processor.git
</code></pre>
<p>Create a new configuration file (.json) following the example below.</p>
<pre><code>    [  
        {  
        "run_example" : {  
              "Tool" : "tool_example",  
              "Args" : {  
                 "param1" : "This is a test",  
                 "param2" : "This is another test"  
              }  
        },  
       "run_example2" : {  
              "Tool" : "tool_example",  
              "Args" : {  
                 "param1" : "run_example",  
                 "param2" : "This is another test"  
        }  
      },  
       "order" : ["run_example", "run_example2"]  
      }
 ]
</code></pre>

