import React from 'react';
import logo from '../assets/logo.svg';

function Home() {
  return (
    <div className="section">
        <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label">Room Code</label>
            </div>
            <div class="field-body">
                <div class="field">
                <p class="control">
                    <input class="input is-static" type="text" value="CODE" />
                </p>
                </div>
            </div>
            </div>

            <div class="field is-horizontal">
            <div class="field-label is-normal">
                <label class="label">To</label>
            </div>
            <div class="field-body">
                <div class="field">
                <p class="control">
                    <input class="input" type="email" placeholder="Recipient email" />
                </p>
                </div>
            </div>
        </div>
    </div>
  );
}

export default Home;
