import {useLayoutEffect, useState} from 'react'
import Top from "./ui/component/pages/Top.jsx";

const windowSize = () => {
    const [size, setSize] = useState([0, 0]);
    useLayoutEffect(() => {
        const updateSize = () => {
            setSize([window.innerWidth, window.innerHeight]);
        };

        window.addEventListener('resize', updateSize);
        updateSize();

        return () => window.removeEventListener('resize', updateSize);
    }, []);
    return size
}




function App() {
    const [width, height] = windowSize()
    return (
        <div className="App">
            <Top windowWidth={width} windowHeight={height}/>
        </div>
    )
}

export default App
