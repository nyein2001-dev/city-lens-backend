import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:5000/')
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div className="App">
            <header className="App-header">
                <h1>Geo Visualization Dashboard</h1>
            </header>
            <main>
                <ol>
                    {data.map(item => (
                        <li key={item.topic}>{item.insight}: {item.country}, {item.title}</li>
                    ))}
                </ol>
            </main>
        </div>
    );
}

export default App;
