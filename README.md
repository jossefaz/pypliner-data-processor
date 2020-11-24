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
<pre class=" language-json"><code class="prism  language-json">        <span class="token punctuation">[</span>  
            <span class="token punctuation">{</span>  
            <span class="token string">"run_example"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                  <span class="token string">"Tool"</span> <span class="token punctuation">:</span> <span class="token string">"tool_example"</span><span class="token punctuation">,</span>  
                  <span class="token string">"Args"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                     <span class="token string">"param1"</span> <span class="token punctuation">:</span> <span class="token string">"This is a test"</span><span class="token punctuation">,</span>  
                     <span class="token string">"param2"</span> <span class="token punctuation">:</span> <span class="token string">"This is another test"</span>  
                  <span class="token punctuation">}</span>  
            <span class="token punctuation">}</span><span class="token punctuation">,</span>  
           <span class="token string">"run_example2"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                  <span class="token string">"Tool"</span> <span class="token punctuation">:</span> <span class="token string">"tool_example"</span><span class="token punctuation">,</span>  
                  <span class="token string">"Args"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                     <span class="token string">"param1"</span> <span class="token punctuation">:</span> <span class="token string">"This is a test 2"</span><span class="token punctuation">,</span>  
                     <span class="token string">"param2"</span> <span class="token punctuation">:</span> <span class="token string">"This is another test 2"</span>  
            <span class="token punctuation">}</span>  
          <span class="token punctuation">}</span><span class="token punctuation">,</span>  
           <span class="token string">"order"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token string">"run_example"</span><span class="token punctuation">,</span> <span class="token string">"run_example2"</span><span class="token punctuation">]</span>  
          <span class="token punctuation">}</span>
     <span class="token punctuation">]</span>
</code></pre>
<p>Now let’s explain the different parameters :</p>
<p>The configuration file is basically a list of Objects (dictionnary), where each of those represents an execution pipeline.</p>
<p>So it begins like a list (<code>[]</code>).<br>
Inside of it we define a global object for each pipelines.<br>
The keys of this object represents the name of the process (feel free to give a name that is very explicit on what this process aims to achieve).</p>
<p>So far we have</p>
<pre class=" language-json"><code class="prism  language-json">        <span class="token punctuation">[</span>
           <span class="token punctuation">{</span>
	           <span class="token string">"run_my_first_script"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>
	           <span class="token punctuation">}</span>
           <span class="token punctuation">}</span>
       <span class="token punctuation">]</span>
</code></pre>
<p>Now we need some mandatory keys to indicates which script this process will execute and what are its arguments.<br>
Let’s add the <code>Tool</code> and <code>Args</code> key :</p>
<pre class=" language-json"><code class="prism  language-json"> <span class="token string">"run_my_first_script"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>
     <span class="token string">"Tool"</span> <span class="token punctuation">:</span> <span class="token string">"tool_example"</span>
      <span class="token string">"Args"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
          <span class="token string">"param1"</span> <span class="token punctuation">:</span> <span class="token string">"This is a test"</span><span class="token punctuation">,</span>  
          <span class="token string">"param2"</span> <span class="token punctuation">:</span> <span class="token string">"This is another test"</span>  
          <span class="token punctuation">}</span>  
  <span class="token punctuation">}</span>
</code></pre>
<p>The <strong><code>Tool</code></strong>  key must be the name of an existing script (that you will build) under the directory <code>Tools</code> -&gt; <code>executables</code> -&gt; <code>&lt;ENVIRONMENT&gt;</code><br>
The <code>ENVIRONMENT</code> is a folder based on the defined runtime environment (dev, prod and test) which is defined by the <code>--env</code> runtime variable (see Run section bellow)</p>
<p>There is a <strong>tool_example</strong> script that you see here is a script that you can find in the <code>Tools</code> -&gt; <code>executables</code> -&gt; <code>dev</code> directory<br>
And this script is very basic :</p>
<pre class=" language-python"><code class="prism  language-python">
<span class="token keyword">def</span> <span class="token function">main</span><span class="token punctuation">(</span>param1<span class="token punctuation">,</span> param2<span class="token punctuation">)</span><span class="token punctuation">:</span>  
  <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"param1 is : "</span><span class="token punctuation">,</span> param1<span class="token punctuation">)</span>  
  <span class="token keyword">print</span><span class="token punctuation">(</span><span class="token string">"param2 is : "</span><span class="token punctuation">,</span> param2<span class="token punctuation">)</span>  
  <span class="token keyword">return</span> param1 <span class="token operator">+</span> <span class="token string">" from main"</span>

</code></pre>
<p>As you can see here : the names of the parameters <strong>must be the sames</strong> as those defined in the configuration file (If it is not the case, an <code>ArgumentMissingException</code> will be raised. This is a custom exception (see Exceptions section bellow)</p>
<p>Each Script must have a <code>main</code> function. But this function could be parameter-less (but if you add parameters to your main function, those parameter’s names must match those in the configuration file)</p>
<p>The <strong>order</strong> list  defines the order in which the pypliner will execute those scripts. So the processes configuration order does not matter, only the <strong>order</strong> list will define the execution order of the scripts.</p>
<h2 id="result-injection">Result injection</h2>
<p>In the world of data processing, it is often necessary to link the results of different processes together: the result of process 1 is used as a basis for process 2 to run.</p>
<p>The pypliner allows you to injects the resulte from one script to another by just writing its name in the configuration :</p>
<pre class=" language-json"><code class="prism  language-json">        <span class="token punctuation">[</span>  
            <span class="token punctuation">{</span>  
            <span class="token string">"run_example1"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                  <span class="token string">"Tool"</span> <span class="token punctuation">:</span> <span class="token string">"tool_example"</span><span class="token punctuation">,</span>  
                  <span class="token string">"Args"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                     <span class="token string">"param1"</span> <span class="token punctuation">:</span> <span class="token string">"This is a test"</span><span class="token punctuation">,</span>  
                     <span class="token string">"param2"</span> <span class="token punctuation">:</span> <span class="token string">"This is another test"</span>  
                  <span class="token punctuation">}</span>  
            <span class="token punctuation">}</span><span class="token punctuation">,</span>  
           <span class="token string">"run_example2"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                  <span class="token string">"Tool"</span> <span class="token punctuation">:</span> <span class="token string">"run_example1"</span><span class="token punctuation">,</span>  <span class="token operator">&lt;&lt;=</span><span class="token operator">===</span> Here we inject the result <span class="token keyword">of</span> run_example1 process that we define before 
                  <span class="token string">"Args"</span> <span class="token punctuation">:</span> <span class="token punctuation">{</span>  
                     <span class="token string">"param1"</span> <span class="token punctuation">:</span> <span class="token string">"This is a test 2"</span><span class="token punctuation">,</span>  
                     <span class="token string">"param2"</span> <span class="token punctuation">:</span> <span class="token string">"This is another test 2"</span>  
            <span class="token punctuation">}</span>  
          <span class="token punctuation">}</span><span class="token punctuation">,</span>  
           <span class="token string">"order"</span> <span class="token punctuation">:</span> <span class="token punctuation">[</span><span class="token string">"run_example"</span><span class="token punctuation">,</span> <span class="token string">"run_example2"</span><span class="token punctuation">]</span> <span class="token operator">&lt;&lt;=</span><span class="token operator">==</span> To be able to inject between processes<span class="token punctuation">,</span> you must keep the order logic too<span class="token punctuation">.</span> You cannot inject the result <span class="token keyword">of</span> a process that you did not execute yet 
          <span class="token punctuation">}</span>
     <span class="token punctuation">]</span>
</code></pre>
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

