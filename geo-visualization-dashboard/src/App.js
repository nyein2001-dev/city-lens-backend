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
        <div className="App min-h-screen bg-gray-100">
            <header className="App-header bg-blue-500 text-white p-4">
                <h1 className="text-2xl font-bold">Geo Visualization Dashboard</h1>
            </header>
            <main className="p-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                    {data.map(item => (
                        <div key={item.topic} className="bg-white shadow-md rounded-xl p-4">
                            <h2 className="text-lg font-semibold">{item.insight}</h2>
                            <h2 className="text-lg font-semibold">{item.country}</h2>
                            <p className="text-gray-600">{item.title}</p>
                        </div>
                    ))}
                </div>
            </main>
        </div>
    );
}

export default App;
