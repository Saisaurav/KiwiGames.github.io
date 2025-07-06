const express = require('express');
const app = express();
const port = process.env.PORT || 8080;

// Serve static files from the 'public' directory
app.use(express.static('public'));

// Example route (optional)
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/HomePage.html');
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});