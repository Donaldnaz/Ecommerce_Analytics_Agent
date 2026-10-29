import React from 'react';
import ReactDOM from 'react-dom/client';
import './App.css';

function App() {
  const metrics = [
    { label: 'Revenue', value: '$245K', trend: '+12.4%' },
    { label: 'Orders', value: '8,420', trend: '+8.1%' },
    { label: 'Conversion', value: '4.7%', trend: '+0.8%' },
    { label: 'AOV', value: '$84.20', trend: '+6.3%' }
  ];

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">CommerceIQ</p>
          <h1>Ecommerce Analytics Agent</h1>
        </div>
        <button className="primary-btn">Generate Report</button>
      </header>

      <section className="metrics-grid">
        {metrics.map((item) => (
          <article key={item.label} className="metric-card">
            <span>{item.label}</span>
            <strong>{item.value}</strong>
            <em>{item.trend}</em>
          </article>
        ))}
      </section>

      <section className="content-grid">
        <div className="panel">
          <h2>Sales Overview</h2>
          <div className="chart-bars">
            <span style={{ height: '35%' }} />
            <span style={{ height: '48%' }} />
            <span style={{ height: '60%' }} />
            <span style={{ height: '52%' }} />
            <span style={{ height: '72%' }} />
            <span style={{ height: '88%' }} />
            <span style={{ height: '96%' }} />
          </div>
        </div>

        <div className="panel">
          <h2>AI Insight</h2>
          <p>
            Conversion rate is outperforming the weekly benchmark in the premium
            apparel category, driven by a surge in repeat customer purchases.
          </p>
        </div>
      </section>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
