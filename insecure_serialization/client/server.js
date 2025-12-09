import express from "express"

const PORT = 3000;
const app = express();

app.use(express.static('public'))

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'))
});

app.listen(PORT, () => {
    console.log(`[SERVER] ExpressJS is listening to port http://localhost:${PORT}`);
});