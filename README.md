# a-simple-neural-network
Neural Network may seems difficult to other programmers who thinks it's full of maths. So here, we are going to develop a simple neural network in python that everyone can understand. Here , am not going to explain more about neural network like weights, cost, back-propogation, batch gradient descent etc

# Train the network
  First of all, we need to train our neural network inorder to undertand our data . Based on training the data into neural network , it will able to predict the values     based on inputs. 
  
  # Training ?
   We humans are trained with every knoweldge from small age . So the knowledge we gain from small age will help us in future to make decisions and predictions.
   for example : we have a exam tomorrow , we need to be well trained to get good marks for the exam likewise we will train the model to get good results.
  # Learning Rate ?
   It decides how fast our model can learn .
   " try a few different values and see which one gives you the best loss without sacrificing speed of training "
  # Accuracy ?  
   Yes ! the results must be accurate . If the results are not accurate there is no use of our neural network. so what should we do here ?
   Yup, we have weights. weights is nothing but a strong connection between neurons. It keeps updating after every training get completed , it is also known as 
   back propogation . In other words, updating weights is called back propogation, after updating the weights it goes back to the network. so when one back                  propogation is complete one traning is complete.
      
   So we have some predicted values . But we need to find errors between the targets and inputs (features) so we need to find avrg of total erros from one                  training (note: we may need to train the model until it is perfect (assume it as an iteration maybe we have 10 iterations we need to find avrg of each erros))
     
  # how to find errors ?
   we have predicted values from training samples and we have actual targets . compare the predicted value with actual targets and subtract it.
   -> predicted - target, this will give erros
  # cost ?
    cost: sum of errors divided by targets 
  
