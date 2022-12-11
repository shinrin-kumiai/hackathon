import * as React from 'react';
import {useLayoutEffect, useState} from "react";
// ここ後で使う可能性があるので残してます
// const windowSize =() => {
//     const [size, setSize] = useState([0, 0])
//     useLayoutEffect(() => {
//         const updateSize = () => {
//             setSize([window.innerWidth, window.innerHeight]);
//         };
//
//         window.addEventListener('resize', updateSize);
//         updateSize();
//
//         return () => window.removeEventListener('resize', updateSize);
//     }, []);
//     return size
// }
