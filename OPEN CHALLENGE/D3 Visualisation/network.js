window.onload = function(){
    

    //Creating the tooltip object in the body
    var tooltip = d3.select("body")
      .append("div")
      .attr('class', 'tooltip');
    
    //Creating the svg object with size 960x540
    var svgCanvas = d3.select("body")
        .append("svg")
        .attr("width", 960)
        .attr("height", 540);
    
    
    
    //Reading the json file 
    // ********** FILE NAME TO BE CHANGED IN BELOW LINE TO READ ANY JSON FILE ********** // 
    
    d3.json("data.json", function(data){

        //Function to return the total amount based on the site name
        function amount_function(site){
            //Variable to return the amount
            var amount = 0
            //Looping each of the links data from the json
            data.links.forEach(function(links) {
                //Checking if either of node01 or node02 is equal to the location input
                if (links.node01 == site || links.node02 == site){
                    //If so, then increase the amount by the value of the amount node
                    amount += links.amount;
                }});
            //Return the amount total
            return amount;
        };
        
        //Function to return x location from the site name
        function x_value(site){
            //Setting value as 0
            var val = 0
            //Looping each of the nodes data
            data.nodes.forEach(function(nodes){
                //Checking if the id from the data is equal to the site name
                if (nodes.id == site){
                    //Setting val to the x location if site name is equal
                    val = nodes.x
                }
            
            });
            //Return the x value
            return val
        }
        
        //Function to return y location from the site name
        function y_value(site){
            //Setting value as 0
            var val = 0
            //Looping each of the nodes data
            data.nodes.forEach(function(nodes){
                //Checking if the id from the data is equal to the site name
                if (nodes.id == site){
                    //Setting val to the y location if site name is equal
                    val = nodes.y
                }
            
            });
            //Return the y value
            return val
        }
        
        //Function to calculate the total number of connections for the site location
        function connections(site){
            //Setting the variable conn to 0
            var conn = 0 
            //Looping through each of the links data
            data.links.forEach(function(links){
                //Checking if either node01 or node02 value is equal to the site location
                if (links.node01 == site || links.node02 == site){
                    //If so, then increment the value by 1
                    conn += 1;
            }});
            //Return the conn value
            return conn
        }
        
        //Function to find the site name from the x and y values
        function site_name(x,y){
            //Setting site as empty string
            var site = ''
            //Looping through the nodes data
            data.nodes.forEach(function(nodes){
                //Checking if x value and y value are same as the input for the site
                if (nodes.x == x && nodes.y == y){
                    //If so, then set the node.id as the site that we need to return
                    site = nodes.id
            }});
            //Return the site name
            return site
        }
          
        //Creating the lines in the svgCanvas using data.links
        svgCanvas.selectAll("line")
            .data(data.links).enter()
            .append("line")
            .attr("x1",function(d){return (x_value(d.node01)) ;}) 
            .attr("y1",function(d){return (y_value(d.node01)) ;}) 
            .attr("x2",function(d){return (x_value(d.node02)) ;})
            .attr("y2",function(d){return (y_value(d.node02)) ;})
            .attr("stroke-width",function(d){return (d.amount/100) ;})
            .attr("stroke","black")
            ;
        
        //Creating the circles in the svgCanvas using data.nodes
        svgCanvas.selectAll("circle")
        .data(data.nodes).enter()
        .append("circle")
        // Setting cx as the d.x value
        .attr("cx",function(d,i){return d.x;}) 
        // Setting cy as the d.y value
        .attr("cy",function(d,i){return d.y;}) 
        //Calculating the amount using the function and dividing it by 60 to set the radius
        .attr("r",function(d){return (amount_function(d.id))/60 ;}) 
        //Setting the stroke as black
        .attr("stroke","black")
        .attr("fill","#B94629")
        //Creating a function for mouseover
        .on("mouseover",function(d){
            //Selecting all the circles
             svgCanvas.selectAll("circle")
                //Setting the opacity to 0.1
                .attr("opacity",0.1)
            //Selecting the circle that the mouse points
             d3.select(this)
                //Setting the opacity to 1
                .attr("opacity",1)
            //Finding the cx and cy position of the circle pointed by the mouse
            var x_val = d3.select(this).attr("cx")
            var y_val = d3.select(this).attr("cy")
            //Finding the site name the mouse is pointing
            var site_n = site_name(x_val,y_val)
            
            //Selecting all the lines
            svgCanvas.selectAll("line")
                //Setting opacity to 0.1
                .attr("opacity",0.1)
            
            //Selecting lines to make the opacity as 1 which are connecting the circle
            d3.select("svg").selectAll("line")
                //Filter the lines which are having either node01 or node02 as the site_n value
                .filter(function(d){
                return d.node01 == site_n || d.node02 == site_n
            })  
                //Setting the opacity to be 1
                .attr("opacity",1)
            
            
            //On mouseover, enabling the tooltip 
            return tooltip.style("visibility", "visible")
                        //Setting the text to be displayed on the tooltip
                        .html("Location : "+ d.id + "<br>Total Amount : "+  amount_function(d.id) + "<br>No. of Connections : " + connections(d.id)).style("opacity",.9);
            
           
         })
        
        //Creating a function for mouse move to display the tooltip
        .on("mousemove", function () {
            return tooltip
                .style("top", (d3.event.pageY + 16) + "px")
                .style("left", (d3.event.pageX + 16) + "px");
        })
        
        //Creating the function to perform action once the mouse is moved away from the circle
        .on("mouseout",function(d){
            //Selecting all the circles and setting opacity to 1
           svgCanvas.selectAll("circle")
             .attr("opacity",1);
            //Selecting all the lines and setting opacity to 1
            svgCanvas.selectAll("line")
                .attr("opacity",1);
            //Making the tooltip as hidden
            return tooltip.style("visibility", "hidden");
         });
        
        
        //Creating text of the  site names using the data.nodes
        svgCanvas.selectAll("text")
            .data(data.nodes).enter()
            .append("text")
            //X value of the text to be same as d.x
            .attr("x",function(d){return d.x;})
            //Setting the Y value to be more than the d.y to display the text below the circle
            .attr("y",function(d){return (d.y +15 + (amount_function(d.id)/60));})
            .attr("text-anchor", "middle")
            //Setting the location name to be d.id
            .text(function(d){return d.id ;})
            .attr("fill","#B94629")
            .style("font-size", "20px")
 
        
    });
    
    
}