import os

BASE = '/Users/cs24/trustyfy-content'

pages = [
    {
        'slug': 'web3-banking',
        'title': 'Web3 Banking — Decentralized Finance for the Modern Era',
        'description': 'Web3 banking lets you control your money without banks. Explore decentralized finance platforms, stablecoin payments, and self-custody wallets for global financial freedom.',
        'h1': 'Web3 Banking',
        'h2': 'What Is Web3 Banking?',
        'sections': [
            ('The Shift to Decentralized Finance',
             'Traditional banking requires permission. A bank can freeze your account, decline your transactions, and limit your financial choices based on algorithms — not people.\n\nWeb3 banking changes this. Built on blockchain infrastructure, it gives you full control over your money without intermediaries. Your funds are held in self-custody wallets, accessible 24/7 from anywhere in the world.',
             'Learn how self-custody works', '/best-self-custody-wallets-2026/'),
            ('Why Web3 Banking Is Growing',
             'Global access: Open an account from any country without residency requirements.\nNo freezes: Self-custody means no platform can freeze your funds based on crypto activity.\nLower fees: Stablecoin transfers bypass traditional banking corridors, reducing costs significantly.\nSpeed: Cross-border transfers settle in minutes, not days.',
             None, None),
            ('What You Can Do With Web3 Banking',
             'Send and receive stablecoins (USDC, USDT) globally.\nConvert between crypto and fiat with Super Swap.\nSpend via Visa card in 180+ countries.\nHold multi-currency balances (USD, EUR, GBP).\nBuild a business banking layer without the restrictions.',
             None, None),
        ],
        'faq': [
            ('What is Web3 banking?', 'Web3 banking is financial infrastructure built on open blockchain protocols. It gives individuals control over their money through self-custody wallets, removing the need for traditional banks as intermediaries.'),
            ('Is Web3 banking safe?', 'Web3 banking is as safe as the practices you follow. Self-custody means you hold your private keys — no platform can freeze your funds. The key is using reputable platforms with transparent policies.'),
            ('How does Web3 banking differ from traditional banking?', 'Traditional banks hold your money and control access. Web3 banking lets you hold your own funds in self-custody wallets. You can move money globally without permission, though you manage your own security.'),
            ('Can I use Web3 banking for business?', 'Yes. Web3 business banking allows companies to hold, send, and receive stablecoins and crypto. Platforms like Trustyfy offer business accounts designed for crypto-native companies.'),
        ]
    },
    {
        'slug': 'non-custodial-wallet',
        'title': 'Non-Custodial Wallet — Your Keys, Your Crypto',
        'description': 'A non-custodial wallet gives you complete control over your digital assets. No bank, no broker, no middleman. Just you and your money. Learn how self-custody works.',
        'h1': 'Non-Custodial Wallet',
        'h2': 'What Is a Non-Custodial Wallet?',
        'sections': [
            ('Full Ownership, Zero Intermediaries',
             'A non-custodial wallet is a cryptocurrency wallet where you — and only you — hold the private keys. Unlike custodial wallets (where a third party holds your keys), non-custodial wallets give you complete, unrestricted control over your funds.\n\nYour assets exist on the blockchain. Your private key is the only proof of ownership. No bank, no platform, no middleman can freeze or access your funds without your permission.',
             None, None),
            ('Why Non-Custodial Matters',
             'Financial sovereignty: You control your money entirely.\nNo counterparty risk: No exchange or platform can collapse with your funds.\nGlobal access: Use your wallet from any device, anywhere.\nCensorship resistance: No authority can freeze or restrict your assets.',
             None, None),
            ('Non-Custodial vs Custodial: What\'s the Difference?',
             'Custodial wallet: A third party (exchange, bank) holds your private keys. You trust them to secure your funds. They can freeze your account.\n\nNon-custodial wallet: You hold the keys. You are the bank. No one can freeze your funds without your private key.',
             None, None),
        ],
        'faq': [
            ('What is a non-custodial wallet?', 'A non-custodial wallet is a cryptocurrency wallet where the user holds and controls the private keys. The user has full ownership of their funds with no third-party intermediary.'),
            ('How is a non-custodial wallet different from a custodial wallet?', 'In a custodial wallet, a third party (like an exchange) holds your private keys. In a non-custodial wallet, you hold the keys yourself — giving you complete control and eliminating counterparty risk.'),
            ('Can I recover my funds if I lose my non-custodial wallet?', 'You can recover your funds using your seed phrase (a list of words generated when you create the wallet). This is why securely storing your seed phrase is critical.'),
            ('What happens if I forget my private key?', 'If you lose access to your non-custodial wallet and don\'t have your seed phrase, your funds are unrecoverable. Unlike banks, there is no password reset or customer support for self-custody wallets.'),
        ]
    },
    {
        'slug': 'self-custody-banking',
        'title': 'Self-Custody Banking — Your Money, Your Rules',
        'description': 'Self-custody banking means you hold your own money — no banks, no freezes, no restrictions. Explore the infrastructure behind financial sovereignty in 2026.',
        'h1': 'Self-Custody Banking',
        'h2': 'What Is Self-Custody Banking?',
        'sections': [
            ('You Are Your Own Bank',
             'Self-custody banking means you hold and control your own money — not a bank, not a platform. Your funds live in self-custody wallets, accessible only to you through your private keys.\n\nThis is the fundamental difference from traditional banking. When you deposit money in a bank, the bank holds it. They can freeze it, limit it, or deny access. With self-custody, only you control what happens to your money.',
             None, None),
            ('The Infrastructure Behind Self-Custody',
             'Self-custody banking runs on open blockchain infrastructure.\n\nWallets: Non-custodial wallets hold your private keys. Only you can authorize transactions.\nStablecoins: Digital dollars (USDC, USDT) that maintain a 1:1 peg to fiat. Your purchasing power is preserved.\nExchange bridges: Convert between crypto and fiat without going through a bank.\nPayment networks: Spend your crypto anywhere Visa is accepted.',
             None, None),
            ('Who Should Use Self-Custody Banking?',
             'Business owners handling international payments.\nDigital nomads needing global financial access.\nCrypto users tired of account freezes.\nAnyone who values financial privacy and sovereignty.\nCompanies operating across borders who need a reliable financial layer.',
             None, None),
        ],
        'faq': [
            ('What is self-custody banking?', 'Self-custody banking is the practice of holding and controlling your own funds through non-custodial wallets and financial infrastructure, without relying on traditional banks to hold your money.'),
            ('Is self-custody banking legal?', 'Yes. Self-custody banking — holding your own funds in non-custodial wallets — is completely legal in most jurisdictions. However, using crypto for illegal activities remains prohibited.'),
            ('What happens if I lose my phone with a self-custody wallet?', 'If your wallet is lost or stolen, you can recover your funds using your seed phrase. Without the seed phrase, funds cannot be recovered. Always store your seed phrase securely offline.'),
            ('Can businesses use self-custody banking?', 'Yes. Many crypto-native businesses use self-custody banking for international payments, payroll, and treasury management. Platforms like Trustyfy offer business accounts designed for this use case.'),
        ]
    },
    {
        'slug': 'stablecoin-payments',
        'title': 'Stablecoin Payments — Send Money Globally for Cents',
        'description': 'Stablecoin payments let you send money anywhere in the world in minutes, for a fraction of the cost of traditional wire transfers. USDC, USDT, and global spending made simple.',
        'h1': 'Stablecoin Payments',
        'h2': 'How Stablecoin Payments Work',
        'sections': [
            ('Instant Global Transfers, Fraction of the Cost',
             'Stablecoin payments use digital currencies (like USDC or USDT) that maintain a 1:1 peg to the US dollar. Unlike regular crypto, their value doesn\'t fluctuate.\n\nWhen you send a stablecoin payment, it settles in minutes — not the 3-5 days of a wire transfer. The cost? Often less than a dollar, regardless of the amount or destination.',
             None, None),
            ('Why Stablecoins Beat Traditional Transfers',
             'Speed: Minutes instead of days.\nCost: A few cents instead of $25-50 per wire.\nAvailability: Send from any crypto wallet to any crypto wallet globally.\nTransparency: Track your payment on-chain in real time.\nNo bank required: Skip the correspondent banking system entirely.',
             None, None),
            ('What You Can Do With Stablecoin Payments',
             'Pay suppliers and contractors internationally.\nReceive payments from clients worldwide.\nSettle invoices in USDC or USDT.\nConvert to local fiat currency via Super Swap.\nSend money to family in any country — no bank account needed.',
             None, None),
        ],
        'faq': [
            ('What is a stablecoin payment?', 'A stablecoin payment is a cryptocurrency transaction using a stablecoin (like USDC or USDT) — a digital currency pegged 1:1 to the US dollar. Payments settle in minutes with minimal fees.'),
            ('How are stablecoin payments different from wire transfers?', 'Wire transfers take 3-5 business days and cost $25-50. Stablecoin payments settle in minutes and cost a fraction of a dollar, regardless of amount or destination.'),
            ('Are stablecoin payments reversible?', 'No. Stablecoin payments are final and irreversible, like cash. Always verify the recipient address before sending.'),
            ('What stablecoins can I use for payments?', 'USDC and USDT are the most widely accepted stablecoins for payments. Both maintain a 1:1 peg to the US dollar.'),
        ]
    },
    {
        'slug': 'decentralized-banking',
        'title': 'Decentralized Banking — Financial Infrastructure Without Banks',
        'description': 'Decentralized banking runs on blockchain protocols instead of traditional banks. Send, hold, and spend money globally without permission, intermediaries, or freezes.',
        'h1': 'Decentralized Banking',
        'h2': 'What Is Decentralized Banking?',
        'sections': [
            ('Banking Without the Bank',
             'Decentralized banking replaces traditional financial infrastructure with blockchain protocols. Instead of banks holding your money, open networks verify and settle transactions.\n\nYou hold your own funds in self-custody wallets. Transactions are verified by distributed networks — no single authority can freeze your account or deny a payment.',
             None, None),
            ('The Core Principles of Decentralized Finance',
             'Open access: Anyone with an internet connection can participate.\nSelf-custody: You hold your own funds — not a bank.\nTransparency: All transactions are verifiable on-chain.\nCensorship resistance: No single authority can restrict your access.\nGlobal reach: Send money anywhere without correspondent banks.',
             None, None),
            ('Decentralized Banking in Practice',
             'Hold stablecoins in non-custody wallets.\nUse decentralized exchanges to convert assets.\nPay globally via stablecoin transfers.\nSpend via crypto-linked Visa cards.\nAccess fiat conversion through non-bank platforms.',
             None, None),
        ],
        'faq': [
            ('What is decentralized banking?', 'Decentralized banking is financial infrastructure built on blockchain protocols that operates without traditional banks. Users hold their own funds in self-custody wallets and interact through open, permissionless networks.'),
            ('How is decentralized banking different from traditional banking?', 'Traditional banking is centralized — banks hold your money and can restrict access. Decentralized banking is distributed — users hold their own funds and no single authority can freeze or control access.'),
            ('Is decentralized banking safe?', 'Decentralized banking is safe when users follow security best practices: protecting private keys, using reputable platforms, and avoiding scams. The technology itself is highly secure due to blockchain encryption.'),
            ('Can I use decentralized banking for business?', 'Yes. Decentralized banking is particularly powerful for businesses — enabling fast, low-cost international payments, transparent transaction records, and financial infrastructure that doesn\'t freeze based on crypto activity.'),
        ]
    },
]

def nl2br(text):
    return text.replace('\n\n', '</p><p class="section-text">').replace('\n', '<br>')

for p in pages:
    slug = p['slug']

    faq_json = ','.join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in p['faq']
    ])
    faq_jsonld = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_json}]}}</script>'

    sections_html = ''
    for heading, text, cta_text, cta_link in p['sections']:
        sections_html += f'''
            <div class="content-section">
                <h2>{heading}</h2>
                <p class="section-text">{nl2br(text)}</p>
                {"<a href=\"" + cta_link + "\" class=\"text-link\">" + cta_text + " →</a>" if cta_text and cta_link else ""}
            </div>'''

    faq_html = ''
    for q, a in p['faq']:
        faq_html += f'''
            <div class="faq-item">
                <h3>{q}</h3>
                <p>{a}</p>
            </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p['title']}</title>
    <meta name="description" content="{p['description']}">
    <link rel="icon" type="image/svg+xml" href="/favicon.svg">
    <meta name="theme-color" content="#000000">
    <meta property="og:title" content="{p['title']}">
    <meta property="og:description" content="{p['description']}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://bankless.living/{slug}/">
    <meta property="og:image" content="https://bankless.living/images/og-default.png">
    <meta property="og:site_name" content="Bankless Living">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@getbankless">
    <meta name="twitter:title" content="{p['title']}">
    <meta name="twitter:description" content="{p['description']}">
    <meta name="twitter:image" content="https://bankless.living/images/og-default.png">
    {faq_jsonld}
    <style>
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
        :root {{
            --black: #000000;
            --white: #ffffff;
            --gray-bg: #f4f8fb;
            --gray-2: #f5f5f7;
            --gray-3: #e8e8ed;
            --gray-4: #86868b;
            --text: #1d1d1f;
            --text-secondary: #6e6e73;
            --blue: #1246c6;
            --blue-hover: #0f38a8;
            --green: #2e7d32;
            --border-radius: 18px;
            --max-width: 1040px;
            --section-padding: 80px;
        }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, sans-serif;
            color: var(--text);
            background: var(--white);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}
        .nav {{ position: fixed; top: 0; left: 0; right: 0; z-index: 1000; background: rgba(255,255,255,0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid rgba(0,0,0,0.06); }}
        .nav-inner {{ max-width: var(--max-width); margin: 0 auto; padding: 0 24px; height: 56px; display: flex; align-items: center; justify-content: space-between; }}
        .nav-logo {{ font-size: 18px; font-weight: 600; color: var(--text); text-decoration: none; letter-spacing: -0.02em; }}
        .nav-links {{ display: flex; gap: 32px; list-style: none; }}
        .nav-links a {{ font-size: 14px; color: var(--text-secondary); transition: color 0.2s; text-decoration: none; }}
        .nav-links a:hover {{ color: var(--text); }}
        .nav-cta {{ background: var(--blue); color: var(--white) !important; padding: 8px 16px; border-radius: var(--border-radius); font-size: 14px !important; transition: background 0.2s; }}
        .nav-cta:hover {{ background: var(--blue-hover); text-decoration: none !important; }}
        .nav-dropdown {{ position: relative; display: inline-block; }}
        .nav-dropdown > a {{ cursor: pointer; display: flex; align-items: center; gap: 4px; font-size: 14px; font-weight: 500; color: var(--text-secondary); }}
        .nav-dropdown > a::after {{ content: ' ▾'; font-size: 11px; }}
        .nav-dropdown-menu {{ display: none; position: absolute; top: calc(100% + 4px); left: 0; background: var(--white); border: 1px solid rgba(0,0,0,0.1); border-radius: 12px; padding: 8px 0; min-width: 220px; box-shadow: 0 8px 30px rgba(0,0,0,0.12); z-index: 1001; }}
        .nav-dropdown:hover > a {{ color: var(--text); }}
        .nav-dropdown:hover .nav-dropdown-menu {{ display: block; }}
        .nav-dropdown-menu a {{ display: block; padding: 10px 16px; font-size: 14px; color: var(--text); white-space: nowrap; transition: background 0.15s; }}
        .nav-dropdown-menu a:hover {{ background: var(--gray-bg); text-decoration: none; }}
        .nav-dropdown-section {{ padding: 8px 16px 4px; font-size: 11px; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 0.05em; }}
        .nav-dropdown-divider {{ height: 1px; background: rgba(0,0,0,0.08); margin: 6px 0; }}
        .hero {{ padding: 160px 24px var(--section-padding); text-align: center; background: var(--white); }}
        .hero-label {{ display: inline-block; font-size: 12px; font-weight: 600; color: var(--blue); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 16px; padding: 6px 12px; background: rgba(18,70,198,0.08); border-radius: 100px; }}
        h1 {{ font-size: clamp(40px, 7vw, 72px); font-weight: 700; line-height: 1.05; letter-spacing: -0.03em; color: var(--text); margin-bottom: 20px; }}
        .hero-sub {{ font-size: clamp(18px, 2.5vw, 22px); color: var(--text-secondary); max-width: 620px; margin: 0 auto 40px; line-height: 1.5; }}
        .hero-cta {{ display: inline-flex; gap: 12px; flex-wrap: wrap; justify-content: center; }}
        .btn-primary {{ display: inline-block; background: var(--blue); color: var(--white); padding: 14px 28px; border-radius: var(--border-radius); font-size: 16px; font-weight: 500; text-decoration: none; transition: background 0.2s, transform 0.2s; }}
        .btn-primary:hover {{ background: var(--blue-hover); text-decoration: none; transform: translateY(-1px); }}
        .btn-secondary {{ display: inline-block; background: var(--gray-bg); color: var(--text); padding: 14px 28px; border-radius: var(--border-radius); font-size: 16px; font-weight: 500; text-decoration: none; transition: background 0.2s; }}
        .btn-secondary:hover {{ background: var(--gray-2); text-decoration: none; }}
        .stats-bar {{ background: var(--gray-bg); padding: 48px 24px; text-align: center; }}
        .stats-grid {{ display: flex; justify-content: center; gap: 64px; flex-wrap: wrap; max-width: var(--max-width); margin: 0 auto; }}
        .stat-item {{ text-align: center; }}
        .stat-value {{ font-size: 36px; font-weight: 700; color: var(--text); letter-spacing: -0.02em; }}
        .stat-label {{ font-size: 14px; color: var(--text-secondary); margin-top: 4px; }}
        .content-wrap {{ max-width: var(--max-width); margin: 0 auto; padding: var(--section-padding) 24px; }}
        .content-section {{ margin-bottom: 64px; padding-bottom: 64px; border-bottom: 1px solid var(--gray-3); }}
        .content-section:last-child {{ border-bottom: none; }}
        .content-section h2 {{ font-size: clamp(26px, 4vw, 36px); font-weight: 700; letter-spacing: -0.02em; margin-bottom: 20px; color: var(--text); }}
        .section-text {{ font-size: 17px; color: var(--text-secondary); line-height: 1.7; max-width: 720px; }}
        .text-link {{ display: inline-block; margin-top: 16px; color: var(--blue); font-size: 15px; font-weight: 500; text-decoration: none; }}
        .text-link:hover {{ text-decoration: underline; }}
        .trust-section {{ padding: var(--section-padding) 24px; background: var(--white); text-align: center; }}
        .trust-section h2 {{ font-size: clamp(28px, 4vw, 40px); font-weight: 700; letter-spacing: -0.02em; margin-bottom: 16px; }}
        .trust-section p {{ font-size: 18px; color: var(--text-secondary); max-width: 560px; margin: 0 auto 32px; }}
        .faq-section {{ background: var(--gray-bg); padding: var(--section-padding) 24px; }}
        .faq-section h2 {{ font-size: clamp(24px, 4vw, 32px); font-weight: 700; letter-spacing: -0.02em; text-align: center; margin-bottom: 48px; }}
        .faq-list {{ max-width: 720px; margin: 0 auto; }}
        .faq-item {{ background: var(--white); border-radius: 12px; padding: 24px; margin-bottom: 16px; }}
        .faq-item h3 {{ font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 8px; }}
        .faq-item p {{ font-size: 15px; color: var(--text-secondary); line-height: 1.6; }}
        footer {{ background: var(--gray-bg); padding: 48px 24px; border-top: 1px solid var(--gray-3); }}
        .footer-inner {{ max-width: var(--max-width); margin: 0 auto; }}
        .footer-top {{ display: flex; justify-content: space-between; align-items: center; padding-bottom: 30px; border-bottom: 1px solid rgba(0,0,0,0.08); margin-bottom: 24px; flex-wrap: wrap; gap: 16px; }}
        .footer-brand {{ font-size: 20px; font-weight: 600; color: var(--text); letter-spacing: -0.02em; }}
        .footer-links {{ display: flex; gap: 24px; list-style: none; flex-wrap: wrap; }}
        .footer-links a {{ font-size: 13px; color: var(--text-secondary); }}
        .footer-links a:hover {{ color: var(--text); text-decoration: none; }}
        .footer-bottom {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }}
        .footer-copy {{ font-size: 12px; color: var(--text-secondary); }}
        .footer-social {{ display: flex; gap: 16px; align-items: center; }}
        .footer-social a {{ font-size: 13px; color: var(--blue); display: flex; align-items: center; gap: 6px; }}
        .footer-social a:hover {{ text-decoration: underline; }}
        @media (max-width: 768px) {{ .nav-links {{ display: none; }} .hero {{ padding: 120px 24px 60px; }} .content-wrap {{ padding: 60px 24px; }} .stats-grid {{ gap: 32px; }} }}
    </style>
</head>
<body>
    <nav class="nav">
        <div class="nav-inner">
            <a href="/" class="nav-logo">Bankless Living</a>
            <ul class="nav-links">
                <li>
                    <div class="nav-dropdown">
                        <a href="/best-self-custody-wallets-2026/">Guides</a>
                        <div class="nav-dropdown-menu">
                            <div class="nav-dropdown-section">All Guides</div>
                            <a href="/best-self-custody-wallets-2026/">Best Self-Custody Wallets 2026</a>
                            <a href="/best-crypto-friendly-banks-2026/">Best Crypto-Friendly Banks 2026</a>
                            <a href="/how-to-open-global-bank-account-2026/">How to Open a Global Bank Account</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nav-dropdown">
                        <a href="/tools/crypto-banking-selector/">Tools</a>
                        <div class="nav-dropdown-menu">
                            <div class="nav-dropdown-section">Interactive Tools</div>
                            <a href="/tools/crypto-banking-selector/">Crypto Banking Selector</a>
                            <a href="/tools/crypto-fiat-calculator/">Crypto vs Fiat Calculator</a>
                            <a href="/tools/self-custody-quiz/">Self-Custody Quiz</a>
                            <div class="nav-dropdown-divider"></div>
                            <a href="/tools/wallet-comparison-matrix/">Wallet Comparison Matrix</a>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="nav-dropdown">
                        <a href="/#about">About</a>
                        <div class="nav-dropdown-menu">
                            <a href="/#about">About Bankless Living</a>
                            <a href="https://app.trustyfy.com?by=101a44">About Trustyfy</a>
                        </div>
                    </div>
                </li>
                <li><a href="https://app.trustyfy.com?by=101a44" class="nav-cta">Get Started</a></li>
            </ul>
        </div>
    </nav>

    <section class="hero">
        <span class="hero-label">Guide</span>
        <h1>{p['h1']}</h1>
        <p class="hero-sub">{p['description']}</p>
        <div class="hero-cta">
            <a href="https://app.trustyfy.com?by=101a44" class="btn-primary">Open Free Account</a>
            <a href="/" class="btn-secondary">Back to Home</a>
        </div>
    </section>

    <div class="stats-bar">
        <div class="stats-grid">
            <div class="stat-item"><div class="stat-value">180+</div><div class="stat-label">Countries Supported</div></div>
            <div class="stat-item"><div class="stat-value">$0</div><div class="stat-label">Account Freeze Policy</div></div>
            <div class="stat-item"><div class="stat-value">&lt;5min</div><div class="stat-label">Global Transfers</div></div>
            <div class="stat-item"><div class="stat-value">0</div><div class="stat-label">Residency Requirements</div></div>
        </div>
    </div>

    <div class="content-wrap">
        {sections_html}
    </div>

    <div class="trust-section">
        <h2>The Bankless-Friendly Banking Layer</h2>
        <p>Trustyfy is the platform that matches the bankless ethos — self-custody, no freezes, global access, multi-chain support.</p>
        <a href="https://app.trustyfy.com?by=101a44" class="btn-primary">Open Free Account</a>
    </div>

    <section class="faq-section">
        <h2>Frequently Asked Questions</h2>
        <div class="faq-list">
            {faq_html}
        </div>
    </section>

    <footer>
        <div class="footer-inner">
            <div class="footer-top">
                <span class="footer-brand">Bankless Living</span>
                <ul class="footer-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/best-self-custody-wallets-2026/">Guides</a></li>
                    <li><a href="/tools/crypto-banking-selector/">Tools</a></li>
                    <li><a href="https://app.trustyfy.com?by=101a44">Trustyfy</a></li>
                    <li><a href="https://t.me/TrustyfyCommunity">Community</a></li>
                </ul>
            </div>
            <div class="footer-bottom">
                <span class="footer-copy">© 2026 Bankless Living Content Hub — Powered by <a href="https://bankless.living">Bankless.Living</a></span>
                <div class="footer-social">
                    <a href="https://x.com/getbankless" target="_blank">Follow @getbankless on X</a>
                    <a href="https://t.me/TrustyfyCommunity">Trustyfy Community</a>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>'''

    dir_path = os.path.join(BASE, slug)
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, 'index.html'), 'w') as f:
        f.write(html)
    print(f'Created: {slug}/')

print('All 5 SEO pages created')