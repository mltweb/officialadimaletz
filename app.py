from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Connect with Me</title>   
                <link rel="icon" href="/static/adi_profile_linke.jpg" type="image/x-icon">     
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
        <script src="https://twgljs.org/dist/4.x/twgl-full.min.js"></script>
        <style>
            body {
                margin: 0;
                font-family: consolas;
                background-color: #1a202c;
                color: white;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }
            #main-content {
                display: flex;
                flex-direction: column;
                align-items: center;
                padding-top: 50px;
                flex: 1;
                z-index: 1;
            }
            .link-button {
    display: flex;
    align-items: center;
    justify-content: left; /* Keep icon and text aligned to the left initially */
    width: 360px;
    padding: 15px;
    margin: 10px 0;
    border-radius: 30px;
    color: white;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.3s ease;
    background-color: #2d3748;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    position: relative;            }
            .link-button:hover {
                background-color: #4a5568;
                transform: translateY(-2px);
            }
            .icon, .svg-icon-wrapper {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-right: 10px; /* Spacing between icon and text */
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff20; /* Semi-transparent background */

            }
            .svg-icon {
                width: 24px;
                height: 24px;
                fill: white;
            }
            .verify-icon {
    width: 20px;
    height: 20px;
    fill: #1DA1F2; /* Twitter blue */
            }
            .arrow {
                animation: pulse 1.5s infinite;
            }
            @keyframes pulse {
                0% { transform: translateY(0); }
                50% { transform: translateY(-5px); }
                100% { transform: translateY(0); }
            }
            footer {
                position: relative;
                text-align: center;
                padding: 20px;
                font-size: 18px;
                color: white;
                z-index: 1;
            }
            #canvas {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                z-index: 0;
                pointer-events: none;
            }
            .link-text {
    flex: 1;
    margin-left: 72px;
}

            .link-text-tiktok {
    flex: 1;
    margin-left: 84px;
}

            .link-text-you {
    flex: 1;
    margin-left: 80px;
}

            .link-text-long {
    flex: 1;
    margin-left: 20px;
}

            .link-text-long1 {
    flex: 1;
    margin-left: 15px;
}

@keyframes glitch {
    0% {
        transform: translate(0);
        opacity: 1;
    }
    20% {
        transform: translate(-2px, -2px);
        opacity: 0.8;
    }
    40% {
        transform: translate(2px, 2px);
        opacity: 1;
    }
    60% {
        transform: translate(-1px, 1px);
        opacity: 0.9;
    }
    80% {
        transform: translate(1px, -1px);
        opacity: 1;
    }
    100% {
        transform: translate(0);
        opacity: 1;
    }
}

@keyframes glitch-shadow {
    0% {
        transform: translate(0);
        opacity: 0.9;
    }
    20% {
        transform: translate(1px, -1px);
        opacity: 0.6;
    }
    40% {
        transform: translate(-1px, 1px);
        opacity: 0.8;
    }
    60% {
        transform: translate(1px, -1px);
        opacity: 0.5;
    }
    80% {
        transform: translate(-1px, 1px);
        opacity: 0.7;
    }
    100% {
        transform: translate(0);
        opacity: 0.9;
    }
}

.animated-link {
    font-weight: bold;
    position: relative;
    color: #1D3756;
    display: inline-block;
    animation: glitch 1s infinite;
}

.animated-link::before,
.animated-link::after {
    content: "SchultzCode";
    position: absolute;
    left: 0;
    color: #4a5568;
    opacity: 0.6;
    clip: rect(0, 100%, 0, 0);
    animation: glitch-shadow 1s infinite;
}

.animated-link::before {
    animation-delay: 0.2s;
}

.animated-link::after {
    animation-delay: 0.4s;
}

        @keyframes cubeBorderColors {
            0% { border-color: red; }
            16.67% { border-color: green; }
            33.33% { border-color: blue; }
            50% { border-color: yellow; }
            66.67% { border-color: white; }
            83.33% { border-color: orange; }
            100% { border-color: red; }
        }

        /* Apply the animated border style to the profile image */
        .animated-border {
            border: 4px solid red; /* Initial border color */
            border-radius: 50%;
            animation: cubeBorderColors 3s linear infinite;
        }


        </style>
    </head>
    <body>

        <!-- Main Content -->
        <div id="main-content">
<div class="relative inline-flex items-center">
            <img src="/static/adi_profile_linke.jpg" alt="Profile" class="w-32 h-32 animated-border">
            <svg class="verify-icon absolute bottom-0 right-0" viewBox="0 0 24 24">
                <path d="M10 15.172l-3.5-3.5 1.415-1.415L10 12.343l5.086-5.086 1.414 1.415z"></path>
            </svg>
</div>            <h1 class="text-3xl font-semibold mt-4">Adi Maletz</h1>
            <p class="text-lg mt-1">Software Developer & Private Jeweler</p>
            <p class="text-sm mt-2 text-gray-400">Connect with me through my official links below</p>
            <p class="text-sm mt-3 text-gray-400 arrow">↓</p>

            <!-- Links Section -->
            <a href="https://www.mltme.com/" class="link-button">
                <img src="/static/MLT_logo.png" alt="MLT" class="icon">
                <span class="link-text-long">MLT Diamonds & Jewelry</span>
            </a>
            <a href="http://www.skool.com/the-golden-vault-3282" class="link-button">
                <img src="/static/the_golden_vault_cover_community.jpg" alt="The Golden Vault" class="icon"> The Golden Vault Community
            </a>
            <a href="https://www.schultzcode.com" class="link-button">
                <img src="/static/schultzcode_logo.jpg" alt="SchultzCode" class="icon">
           <span class="link-text-long1">SchultzCode Technologies</span>
            </a>
            <a href="https://www.tiktok.com/@adi_maletz?_t=8qUQJ9wwDpZ&_r=1" class="link-button">
                <div class="svg-icon-wrapper">
                    <svg class="svg-icon" enable-background="new 0 0 24 24" viewBox="0 0 24 24">
                        <title>TikTok</title>
                        <path d="M9.37,23.5a7.468,7.468,0,0,1,0-14.936.537.537,0,0,1,.538.5v3.8a.542.542,0,0,1-.5.5,2.671,2.671,0,1,0,2.645,2.669.432.432,0,0,1,0-.05V1a.5.5,0,0,1,.5-.5h3.787a.5.5,0,0,1,.5.5A4.759,4.759,0,0,0,21.59,5.76a.5.5,0,0,1,.5.5L22.1,10a.533.533,0,0,1-.519.515,9.427,9.427,0,0,1-4.741-1.268v6.789A7.476,7.476,0,0,1,9.37,23.5ZM8.908,9.585a6.466,6.466,0,1,0,6.93,6.447V8.326a.5.5,0,0,1,.791-.407A8.441,8.441,0,0,0,21.1,9.5l-.006-2.76A5.761,5.761,0,0,1,15.859,1.5H13.051V16.032a.458.458,0,0,1,0,.053,3.672,3.672,0,1,1-4.14-3.695Z"></path>
                    </svg>
                </div>
                <span class="link-text-tiktok">TikTok</span>
            </a>
            <a href="https://www.youtube.com/@mlt_diamond_jewelry" class="link-button">
                <div class="svg-icon-wrapper">
                    <svg class="svg-icon" enable-background="new 0 0 24 24" viewBox="0 0 24 24">
                        <title>YouTube</title>
                        <path d="M12,20.55c-.3,0-7.279-.006-9.115-.5A3.375,3.375,0,0,1,.5,17.665,29.809,29.809,0,0,1,0,12,29.824,29.824,0,0,1,.5,6.334,3.375,3.375,0,0,1,2.885,3.948c1.836-.492,8.819-.5,9.115-.5s7.279.006,9.115.5A3.384,3.384,0,0,1,23.5,6.334,29.97,29.97,0,0,1,24,12a29.97,29.97,0,0,1-.5,5.666,3.384,3.384,0,0,1-2.388,2.386C19.279,20.544,12.3,20.55,12,20.55Zm0-16.1c-.072,0-7.146.006-8.857.464A2.377,2.377,0,0,0,1.464,6.593,29.566,29.566,0,0,0,1,12a29.566,29.566,0,0,0,.464,5.407,2.377,2.377,0,0,0,1.679,1.679c1.711.458,8.785.464,8.857.464s7.146-.006,8.857-.464a2.377,2.377,0,0,0,1.679-1.679A29.66,29.66,0,0,0,23,12a29.66,29.66,0,0,0-.464-5.407h0a2.377,2.377,0,0,0-1.679-1.679C19.146,4.456,12.071,4.45,12,4.45ZM9.7,15.95a.5.5,0,0,1-.5-.5V8.55a.5.5,0,0,1,.75-.433l5.975,3.45a.5.5,0,0,1,0,.866L9.95,15.883A.5.5,0,0,1,9.7,15.95Zm.5-6.534v5.168L14.675,12Z"></path>
                    </svg>
                </div> 
                <span class="link-text-you">YouTube</span>
            </a>
            <a href="https://www.instagram.com/officialadimaletz/" class="link-button">
                <div class="svg-icon-wrapper">
                    <svg class="svg-icon" enable-background="new 0 0 24 24" viewBox="0 0 24 24">
                        <title>Instagram</title>
                        <path d="M21.938,7.71a7.329,7.329,0,0,0-.456-2.394,4.615,4.615,0,0,0-1.1-1.694,4.61,4.61,0,0,0-1.7-1.1,7.318,7.318,0,0,0-2.393-.456C15.185,2.012,14.817,2,12,2s-3.185.012-4.29.062a7.329,7.329,0,0,0-2.394.456,4.615,4.615,0,0,0-1.694,1.1,4.61,4.61,0,0,0-1.1,1.7A7.318,7.318,0,0,0,2.062,7.71C2.012,8.814,2,9.182,2,12s.012,3.186.062,4.29a7.329,7.329,0,0,0,.456,2.394,4.615,4.615,0,0,0,1.1,1.694,4.61,4.61,0,0,0,1.7,1.1,7.318,7.318,0,0,0,2.393.456c1.1.05,1.472.062,4.29.062s3.186-.012,4.29-.062a7.329,7.329,0,0,0,2.394-.456,4.9,4.9,0,0,0,2.8-2.8,7.318,7.318,0,0,0,.456-2.393c.05-1.1.062-1.472.062-4.29S21.988,8.814,21.938,7.71Zm-1,8.534a6.351,6.351,0,0,1-.388,2.077,3.9,3.9,0,0,1-2.228,2.229,6.363,6.363,0,0,1-2.078.388C15.159,20.988,14.8,21,12,21s-3.159-.012-4.244-.062a6.351,6.351,0,0,1-2.077-.388,3.627,3.627,0,0,1-1.35-.879,3.631,3.631,0,0,1-.879-1.349,6.363,6.363,0,0,1-.388-2.078C3.012,15.159,3,14.8,3,12s.012-3.159.062-4.244A6.351,6.351,0,0,1,3.45,5.679a3.627,3.627,0,0,1,.879-1.35A3.631,3.631,0,0,1,5.678,3.45a6.363,6.363,0,0,1,2.078-.388C8.842,3.012,9.205,3,12,3s3.158.012,4.244.062a6.351,6.351,0,0,1,2.077.388,3.627,3.627,0,0,1,1.35.879,3.631,3.631,0,0,1,.879,1.349,6.363,6.363,0,0,1,.388,2.078C20.988,8.841,21,9.2,21,12S20.988,15.159,20.938,16.244Z"></path>
                        <path d="M17.581,5.467a.953.953,0,1,0,.952.952A.954.954,0,0,0,17.581,5.467Z"></path>
                        <path d="M12,7.073A4.927,4.927,0,1,0,16.927,12,4.932,4.932,0,0,0,12,7.073Zm0,8.854A3.927,3.927,0,1,1,15.927,12,3.932,3.932,0,0,1,12,15.927Z"></path>
                    </svg>
                </div> 
                 <span class="link-text">Instegram</span>
            </a>
        </div>

        <!-- Shader Canvas for Footer Effect -->
        <canvas id="canvas"></canvas>

        <!-- Footer Information -->
        <footer>
    &copy; 2025 All rights reserved. Design by 
    <a href="https://www.schultzcode.com" style="color: white;" class="animated-link">SchultzCode</a>
        </footer>

        <!-- Vertex Shader -->
        <script id="vertexShader" type="x-shader/x-vertex">
            attribute vec4 position;
            void main() {
                gl_Position = vec4(position);
            }
        </script>

        <!-- Fragment Shader -->
        <script id="fragmentShader" type="x-shader/x-fragment">
            #ifdef GL_FRAGMENT_PRECISION_HIGH
            precision highp float;
            #else
            precision mediump float;
            #endif

            uniform vec2 u_resolution;
            uniform float u_time;
            uniform vec2 u_mouse;

            vec2 random2(vec2 st){
                st = vec2(dot(st, vec2(127.1, 311.7)), dot(st, vec2(269.5, 183.3)));
                return -1.0 + 2.0 * fract(sin(st) * 43758.5453123);
            }
            float noise(vec2 st) {
                vec2 i = floor(st);
                vec2 f = fract(st);
                vec2 u = f * f * (3.0 - 2.0 * f);
                return mix(
                    mix(dot(random2(i + vec2(0.0, 0.0)), f - vec2(0.0, 0.0)),
                        dot(random2(i + vec2(1.0, 0.0)), f - vec2(1.0, 0.0)), u.x),
                    mix(dot(random2(i + vec2(0.0, 1.0)), f - vec2(0.0, 1.0)),
                        dot(random2(i + vec2(1.0, 1.0)), f - vec2(1.0, 1.0)), u.x), u.y);
            }

            void main() {
                vec2 uv = gl_FragCoord.xy / u_resolution;
                float waveOffset = 0.3;
                float waveCenter = 1.0;
                float waveFocus = 0.25;
                float waveSpeed = 2.0;
                float wMin = waveCenter - waveFocus;
                float wMax = waveCenter + waveFocus;

                uv.x *= u_resolution.x / u_resolution.y;
                uv.y *= 2.0;

                vec3 baseColor = vec3(26.0 / 255.0, 32.0 / 255.0, 44.0 / 255.0);

                float rn = noise(vec2(uv.x, u_time / waveSpeed));
                float ry = uv.y - rn;
                float r = smoothstep(wMin, wMax, ry);

                float bn = noise(vec2(uv.x, u_time / waveSpeed - waveOffset));
                float by = uv.y - bn;
                float b = smoothstep(wMin, wMax, by);

                float gn = noise(vec2(uv.x, u_time / waveSpeed + waveOffset));
                float gy = uv.y - gn;
                float g = smoothstep(wMin, wMax, gy);

                gl_FragColor = vec4(baseColor.r * r, baseColor.g * g, baseColor.b * b, 1.0);
            }
        </script>

        <!-- JavaScript for WebGL -->
        <script>
            const gl = document.getElementById("canvas").getContext("webgl");
            const programInfo = twgl.createProgramInfo(gl, ["vertexShader", "fragmentShader"]);
            const arrays = { position: [-1, -1, 0, 1, -1, 0, -1, 1, 0, -1, 1, 0, 1, -1, 0, 1, 1, 0] };
            const bufferInfo = twgl.createBufferInfoFromArrays(gl, arrays);

            let mouseX = 0, mouseY = 0;
            document.getElementById("canvas").addEventListener('mousemove', e => {
                mouseX = e.clientX;
                mouseY = e.clientY;
            });

            function render(time) {
                twgl.resizeCanvasToDisplaySize(gl.canvas, window.devicePixelRatio);
                gl.viewport(0, 0, gl.canvas.width, gl.canvas.height);
                const uniforms = {
                    u_time: time * 0.002,
                    u_resolution: [gl.canvas.width, gl.canvas.height],
                    u_mouse: [mouseX, mouseY],
                };
                gl.useProgram(programInfo.program);
                twgl.setBuffersAndAttributes(gl, programInfo, bufferInfo);
                twgl.setUniforms(programInfo, uniforms);
                gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
                requestAnimationFrame(render);
            }
            requestAnimationFrame(render);
        </script>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
