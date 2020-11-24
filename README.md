---


---

<h1 id="pypliner-data-processor">Pypliner-data-processor</h1>
<p>The aim of this project is to allow a great modularity in the development of data processes based on the execution sequence of scripts.</p>
<p>The original idea was to provide a central script that would receive as input a configuration file, from which it would be able to import and execute the different scripts.</p>
<p>The power of this tool lies in the fact that it allows to inject the result of a given script to a target script as a parameter. All this based only on the simple configuration file (JSON).</p>
<h1 id="install">Install</h1>
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
                 "param1" : "This is a test",  
                 "param2" : "This is another test"  
        }  
      },  
       "order" : ["run_example", "run_example2"]  
      }
 ]
</code></pre>
<p>Now let’s explain the different parameters :</p>
<p>The configuration file is basically a list of Objects (dictionnary), where each of those represents an execution pipeline.</p>
<p>So it begins like a list (<code>[]</code>).<br>
Inside of it we define a global object for each pipelines.<br>
The keys of this object represents the name of the process (feel free to give a name that is very explicit on what this process aims to achieve).</p>
<p>So far we have</p>
<pre><code>    [
       {
           "run_my_first_script" : {
           }
       }
   ]
</code></pre>
<p>Now we need some mandatory keys to indicates which script this process will execute and what are its arguments.<br>
Let’s add the <code>Tool</code> and <code>Args</code> key :</p>
<pre><code> "run_my_first_script" : {
     "Tool" : "tool_example"
      "Args" : {  
          "param1" : "This is a test",  
          "param2" : "This is another test"  
          }  
  }
</code></pre>
<p>The <strong><code>Tool</code></strong>  key must be the name of an existing script (that you will build) under the directory <code>Tools</code> -&gt; <code>executables</code> -&gt; <code>&lt;ENVIRONMENT&gt;</code><br>
The <code>ENVIRONMENT</code> is a folder based on the defined runtime environment (dev, prod and test) which is defined by the <code>--env</code> runtime variable (see Run section bellow)</p>
<h1 id="run">Run</h1>
<h2 id="runtime-variables">Runtime variables</h2>
<ul>
<li>
<p><code>--logpath</code>, <code>-lp</code> : path for writting logs (default value is defined<br>
to 	‘<code>./logs</code>’ i.e the running directory)</p>
</li>
<li>
<p><code>--logconfig</code>, <code>-lc</code> : path for configuring the logs file (this projects come with a default logger configuration file that you can use as a base for your own logger configuration definition. So this variable has a default value of "“Config/prod/logger.json”)</p>
</li>
<li>
<p><code>--config</code>, <code>-cfg</code> : path of the configuration file</p>
</li>
<li>
<p><code>--env</code>, <code>-e</code> : define the environment of the runtime (‘DEV’, ‘PROD’, ‘TEST’ are the possible values and it has a default value of ‘DEV’)</p>
</li>
</ul>

