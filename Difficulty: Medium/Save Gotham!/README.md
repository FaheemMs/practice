<h2><a href="https://www.geeksforgeeks.org/problems/save-gotham1222/1?page=1&category=Stack&difficulty=Medium&status=unsolved&sortBy=difficulty">Save Gotham!</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Gotham has been attacked by Joker . Bruce Wayne has deployed an automatic machine gun at each tower of Gotham. All the towers in Gotham are in a straight line. You are given no of towers&nbsp;<strong>n</strong> followed by the heights of <strong>n</strong> towers.<br>For every tower <strong>p</strong>, find the height of the closest tower (towards the right), greater than the height of the tower <strong>p</strong>. Now, print the sum of all such heights (mod 1000000001).</span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> If for a tower <strong>k</strong>, no such tower exists then take its height as 0.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> arr[]= {112, 133, 161, 311, 122, 
                    512, 1212, 0, 19212}
<strong>Output :</strong> 41265
<strong>Explanation:</strong>
nextgreater(112) : 133
nextgreater(133) : 161
nextgreater(161) : 311
nextgreater(311) : 512
nextgreater(122) : 512
nextgreater(512) : 1212
nextgreater(1212) : 19212
nextgreater(0) : 19212
nextgreater(19212) : 0
add = 133+161+311+512+512+1212+19212+19212+0 
add = 41265.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> arr[] = {5, 9, 7, 6} <strong>
Output :</strong>  9
</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>save_gotham()</strong> that takes an array <strong>(arr)</strong>, sizeOfArray <strong>(n)</strong>, and return the sum of next greater element of every element. The driver code takes care of the printing.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong>&nbsp;O(N).<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(N).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup><br>0 ≤ A[i] ≤ 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Stack</code>&nbsp;<code>Data Structures</code>&nbsp;