import { useWallet } from '@solana/wallet-adapter-react';
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui';
import { useEffect, useState } from 'react';

function App() {
  const { publicKey } = useWallet();

  const [mint, setMint] = useState('');
  const [balance, setBalance] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [tokens, setTokens] = useState<{ symbol: string; mint: string }[]>([]);

  // Завантаження токенів
  useEffect(() => {
    fetch('http://localhost:8000/tokens')
      .then((res) => res.json())
      .then((data) => setTokens(data))
      .catch(() => setTokens([]));
  }, []);

  const fetchBalance = async () => {
    if (!publicKey) return;
    setLoading(true);
    setError('');
    setBalance(null);

    try {
      const url = new URL('http://localhost:8000/balance');
      url.searchParams.append('address', publicKey.toBase58());
      if (mint.trim() !== '') {
        url.searchParams.append('mint', mint.trim());
      }

      const res = await fetch(url.toString());
      const data = await res.json();

      if (res.ok) {
        setBalance(data.balance);
      } else {
        setError(data.detail || 'Error');
      }
    } catch (err) {
      setError('Failed to fetch balance.');
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: '2rem', color: 'white', fontFamily: 'Arial' }}>
      <WalletMultiButton />

      {publicKey && (
        <div style={{ marginTop: '2rem' }}>
          <div>
            <strong>Wallet:</strong> {publicKey.toBase58()}
          </div>

          {/* Вибір токена */}
          <div style={{ marginTop: '1rem' }}>
            <label>
              Select token:{' '}
              <select
                value={mint}
                onChange={(e) => setMint(e.target.value)}
                style={{ padding: '0.5rem', width: '300px' }}
              >
                <option value="">-- SOL (native) --</option>
                {tokens.map((t) => (
                  <option key={t.mint} value={t.mint}>
                    {t.symbol}
                  </option>
                ))}
              </select>
            </label>
          </div>

          {/* Поле ручного введення (опціональне) */}
          <div style={{ marginTop: '1rem' }}>
            <label>
              Mint Address (optional):{' '}
              <input
                type="text"
                placeholder="leave empty for SOL"
                value={mint}
                onChange={(e) => setMint(e.target.value)}
                style={{ padding: '0.5rem', width: '400px' }}
              />
            </label>
          </div>

          <button
            onClick={fetchBalance}
            style={{
              marginTop: '1rem',
              padding: '0.5rem 1rem',
              backgroundColor: '#7c3aed',
              color: 'white',
              border: 'none',
              cursor: 'pointer',
            }}
          >
            {loading ? 'Loading...' : 'Get Balance'}
          </button>

          {balance !== null && (
            <div style={{ marginTop: '1rem' }}>
              <strong>Balance:</strong> {balance}
            </div>
          )}

          {error && (
            <div style={{ marginTop: '1rem', color: 'red' }}>
              <strong>Error:</strong> {error}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
