import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------
# Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="Business Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# Custom CSS
# ----------------------------------------
st.markdown("""
<style>
/* ==========================
APP BACKGROUND
========================== */

.stApp{

background:
linear-gradient(
135deg,
#0F172A 0%,
#111827 35%,
#1E293B 100%
);

background-attachment:fixed;

}
/* ==========================
STREAMLIT HEADER
========================== */

[data-testid="stHeader"]{
    background:#0F172A !important;
    border:none !important;
    box-shadow:none !important;
}

header{
    background:#0F172A !important;
}

[data-testid="stToolbar"]{
    background:#0F172A !important;
}
            /* ==========================
SIDEBAR COLLAPSE BUTTON
========================== */

/* ==========================
SIDEBAR TOGGLE BUTTON
========================== */

/* Open sidebar button */
div[data-testid="stSidebarCollapsedControl"] button,
div[data-testid="stSidebarCollapseButton"] button{
    background:#7C3AED !important;
    color:white !important;
    border-radius:12px !important;
    border:none !important;
}

/* Both arrow icons */
div[data-testid="stSidebarCollapsedControl"] svg,
div[data-testid="stSidebarCollapseButton"] svg{
    color:white !important;
    fill:white !important;
    stroke:white !important;
}

/* Hover effect */
div[data-testid="stSidebarCollapsedControl"] button:hover,
div[data-testid="stSidebarCollapseButton"] button:hover{
    background:#8B5CF6 !important;
}
            /* Hide the default arrow */
[data-testid="stSidebarCollapsedControl"] svg,
[data-testid="stSidebarCollapseButton"] svg{
    opacity:0 !important;
}

/* Show hamburger icon */
[data-testid="stSidebarCollapsedControl"] button::before,
[data-testid="stSidebarCollapseButton"] button::before{
    content:"☰";
    color:white;
    font-size:26px;
    font-weight:bold;
    position:absolute;
    left:50%;
    top:50%;
    transform:translate(-50%, -50%);
}

/* Purple button */
[data-testid="stSidebarCollapsedControl"] button,
[data-testid="stSidebarCollapseButton"] button{
    position:relative;
    width:46px !important;
    height:46px !important;
    background:#7C3AED !important;
    border-radius:12px !important;
    border:none !important;
}
/* ===================================
KEEP HAMBURGER ALWAYS ON LEFT
=================================== */

/* Position the button */
[data-testid="stSidebarCollapseButton"]{
    position: absolute !important;
    left: 12px !important;
    top: 12px !important;
    right: auto !important;
}

/* Style the button */
[data-testid="stSidebarCollapseButton"] button{
    width:48px !important;
    height:48px !important;
    border-radius:12px !important;
    background:#7C3AED !important;
    border:none !important;
}

/* Hide default arrow */
[data-testid="stSidebarCollapseButton"] svg{
    display:none !important;
}

/* Show hamburger */
[data-testid="stSidebarCollapseButton"] button::before{
    content:"☰";
    color:white;
    font-size:28px;
    font-weight:bold;
    line-height:48px;
    display:block;
    text-align:center;
}
                      
footer{
visibility:hidden;
}

.main .block-container{

padding-top:2rem;

padding-left:2rem;

padding-right:2rem;

padding-bottom:2rem;

max-width:1450px;

}   
/* ==========================
PREMIUM SIDEBAR
========================== */

section[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#111827,
#1E293B
);

border-right:1px solid rgba(255,255,255,.08);

}

section[data-testid="stSidebar"] label{

color:white !important;

font-weight:600;

font-size:15px;

}

section[data-testid="stSidebar"] .stSelectbox{

margin-bottom:12px;

}

section[data-testid="stSidebar"] .stDownloadButton button,
section[data-testid="stSidebar"] .stButton button{

background:linear-gradient(90deg,#7C3AED,#2563EB);

border:none;

color:white;

border-radius:12px;

font-weight:600;

}        
/* ==========================
PREMIUM KPI CARDS
========================== */

.metric-card{

background:linear-gradient(135deg,#16213E,#0F172A);

border:1px solid rgba(255,255,255,.08);

border-radius:20px;

padding:25px;

transition:.3s;

box-shadow:0px 10px 30px rgba(0,0,0,.35);

margin-bottom:15px;

}

.metric-card:hover{

transform:
translateY(-8px)
scale(1.04);

border:1px solid #8B5CF6;

box-shadow:
0 0 20px rgba(139,92,246,.45),
0 15px 40px rgba(0,0,0,.45);

transition:.35s ease;

cursor:pointer;

}
.chart-card{

background:rgba(17,24,39,.70);

backdrop-filter:blur(20px);

border-radius:22px;

padding:15px;

border:1px solid rgba(255,255,255,.08);

box-shadow:0 15px 35px rgba(0,0,0,.35);

margin-bottom:20px;

transition:.35s;

}

.chart-card:hover{

transform:translateY(-5px);

box-shadow:
0 0 25px rgba(124,58,237,.30),
0 15px 40px rgba(0,0,0,.45);

}
.metric-title{

font-size:14px;

color:#A5B4FC;

text-transform:uppercase;

letter-spacing:1px;

margin-bottom:12px;

}

.metric-value{

font-size:38px;

font-weight:800;

color:white;

letter-spacing:1px;

}
.metric-growth{

margin-top:10px;

font-size:14px;

color:#22C55E;

}
.stButton>button,
.stDownloadButton>button{

width:100%;

height:48px;

border:none;

border-radius:14px;

background:linear-gradient(90deg,#7C3AED,#2563EB);

color:white;

font-size:15px;

font-weight:600;

transition:.3s;

}

.stButton>button:hover,
.stDownloadButton>button:hover{

transform:translateY(-3px);

box-shadow:0 0 18px rgba(124,58,237,.45);

}
.stApp{
    background:linear-gradient(
        180deg,
        #0F172A,
        #111827,
        #1E293B
    );
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------
# Title
# ----------------------------------------

from datetime import datetime

today = datetime.now().strftime("%d %B %Y")

st.markdown(f"""
<div style="
background:linear-gradient(
135deg,
rgba(30,41,59,.95),
rgba(15,23,42,.95)
);
padding:35px;
border-radius:25px;
border:1px solid rgba(255,255,255,0.08);
box-shadow:
0 15px 40px rgba(0,0,0,.55),
0 0 25px rgba(124,58,237,.15);
margin-bottom:25px;
">

<h1 style="
color:white;
font-size:42px;
margin-bottom:5px;
font-weight:700;
">
📊 Business Insights Dashboard
</h1>

<h3 style="
color:#8B5CF6;
margin-top:0px;
">
Retail Sales Analytics Platform
</h3>

<p style="
color:#CBD5E1;
font-size:18px;
">
Analyze sales performance, customer behavior, and business trends using interactive visualizations.
</p>

<p style="
color:#94A3B8;
font-size:15px;
">
📅 {today}
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv(
    "superstore.csv",
    encoding="latin1"
)
# ============================================
# PREMIUM CHART THEME
# ============================================

def premium_chart(fig, title):

    fig.update_layout(

        title=dict(
            text=title,
            x=0.02,
            font=dict(
                size=22,
                color="white",
                family="Poppins"
            )
        ),

        template="plotly_dark",

    paper_bgcolor="#1B2338",

    plot_bgcolor="#1B2338",

        font=dict(
            color="white",
            family="Poppins",
            size=13
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        height=420,

        hoverlabel=dict(
            bgcolor="#6D28D9",
            font_size=14,
            font_color="white"
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

    )

    fig.update_xaxes(

        showgrid=True,
        gridcolor="rgba(148,163,184,.15)",
        gridwidth=1,
        zeroline=False

    )

    fig.update_yaxes(

        showgrid=True,
        gridcolor="rgba(148,163,184,.15)",
        gridwidth=1,
        zeroline=False

    )

    return fig

def format_number(value):

    if value >= 1_000_000:
        return f"${value/1_000_000:.2f}M"

    elif value >= 1_000:
        return f"${value/1_000:.1f}K"

    return f"${value:.0f}"
# ----------------------------------------
# Sidebar Filters
# ----------------------------------------

st.sidebar.markdown("""
<div style='text-align:center;padding:10px 0;'>

<h2 style='color:white;margin-bottom:5px;'>
📊 Business Insights
</h2>

<p style='color:#A5B4FC;font-size:14px;'>
Dashboard Filters
</p>

</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")



regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())
states = ["All"] + sorted(df["State"].dropna().unique().tolist())
segments = ["All"] + sorted(df["Segment"].dropna().unique().tolist())
categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())

selected_region = st.sidebar.selectbox("🌍 Select Region", regions)
selected_state = st.sidebar.selectbox("🏙️ Select State", states)
selected_segment = st.sidebar.selectbox("👥 Select Segment", segments)
selected_category = st.sidebar.selectbox("📂 Select Category", categories)

# ----------------------------------------
# Apply Filters
# ----------------------------------------

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[filtered_df["Region"] == selected_region]

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["State"] == selected_state]

if selected_segment != "All":
    filtered_df = filtered_df[filtered_df["Segment"] == selected_segment]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# ----------------------------------------
# KPI Values
# ----------------------------------------

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].count()
total_customers = filtered_df["Customer Name"].nunique()

st.sidebar.markdown("---")

st.sidebar.markdown(f"""
<div style="
background:linear-gradient(135deg,#1E293B,#111827);
padding:18px;
border-radius:18px;
border:1px solid rgba(255,255,255,.08);
">

<h3 style="color:white;">📊 Dashboard Summary</h3>

<p style="color:#CBD5E1;">
💰 Sales: <b>{format_number(total_sales)}</b>
</p>

<p style="color:#CBD5E1;">
📈 Profit: <b>{format_number(total_profit)}</b>
</p>

<p style="color:#CBD5E1;">
📦 Orders: <b>{total_orders:,}</b>
</p>

<p style="color:#CBD5E1;">
👥 Customers: <b>{total_customers}</b>
</p>

</div>
""", unsafe_allow_html=True)

# ----------------------------------------
# KPI Cards
# ----------------------------------------
st.markdown("""
<div style="
background:rgba(17,24,39,0.65);
padding:25px;
border-radius:24px;
border:1px solid rgba(255,255,255,.08);
backdrop-filter:blur(18px);
box-shadow:0 15px 35px rgba(0,0,0,.35);
margin-bottom:25px;
">
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Total Sales</div>
        <div class="metric-value">{format_number(total_sales)}</div>
        <div class="metric-growth">▲ +12.4%</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈 Total Profit</div>
        <div class="metric-value">{format_number(total_profit)}</div>
        <div class="metric-growth">▲ +8.7%</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📦 Orders</div>
        <div class="metric-value">{total_orders}</div>
        <div class="metric-growth">▲ +5.1%</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👥 Customers</div>
        <div class="metric-value">{total_customers}</div>
        <div class="metric-growth">▲ +9.8%</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

st.write("")
# ============================================
# CHART SECTION
# ============================================

st.markdown("<br>", unsafe_allow_html=True)

chart1, chart2 = st.columns([2,1])
st.markdown("""
<div style="
background:rgba(17,24,39,0.70);
padding:20px;
border-radius:24px;
border:1px solid rgba(255,255,255,.08);
box-shadow:0 15px 35px rgba(0,0,0,.35);
margin-bottom:25px;
">
""", unsafe_allow_html=True)
# -----------------------------
# Monthly Sales Trend
# -----------------------------

filtered_df["Order Date"] = pd.to_datetime(
    filtered_df["Order Date"],
    format="mixed",
    errors="coerce"
)

monthly_sales = (
    filtered_df
    .groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig_month = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    markers=True
)

fig_month.update_traces(

    line=dict(
        color="#7C3AED",
        width=5,
        shape="spline"
    ),

    marker=dict(
        size=10,
        color="#A855F7",
        line=dict(
            color="white",
            width=2
        )
    ),

    hovertemplate=
    "<b>%{x}</b><br>" +
    "Sales: <b>$%{y:,.0f}</b><extra></extra>"

)

premium_chart(
    fig_month,
    f"📈 Monthly Sales Trend ({selected_region})"
)



# -----------------------------
# Sales by Category
# -----------------------------

category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig_category = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    hole=0.70,
    color="Category",
    color_discrete_sequence=[
        "#8B5CF6",
        "#3B82F6",
        "#F97316"
    ]
)

fig_category.update_traces(
    textinfo="percent+label",
    textfont=dict(
        size=14,
        color="white"
    ),
    pull=[0.02, 0.02, 0.02],
    marker=dict(
        line=dict(
            color="#111827",
            width=3
        )
    ),
    hovertemplate="<b>%{label}</b><br>"
                  "Sales: <b>$%{value:,.0f}</b><br>"
                  "Share: %{percent}<extra></extra>"
)

premium_chart(
    fig_category,
    f"🥧 Sales by Category ({selected_region})"
)

fig_category.update_layout(
    annotations=[
        dict(
            text="<b>Sales</b>",
            x=0.5,
            y=0.5,
            showarrow=False,
            font=dict(
                size=22,
                color="white"
            )
        )
    ]
)

with chart1:

    st.plotly_chart(fig_month, use_container_width=True)

with chart2:

    st.plotly_chart(
        fig_category,
        width="stretch"
    )
st.markdown("</div>", unsafe_allow_html=True)
# ============================================
# ANALYTICS SECTION
# ============================================

row1, row2, row3 = st.columns([1.1, 1, 1])
st.markdown("""
<div style="
background:rgba(17,24,39,0.70);
padding:20px;
border-radius:24px;
border:1px solid rgba(255,255,255,.08);
box-shadow:0 15px 35px rgba(0,0,0,.35);
margin-bottom:25px;
">
""", unsafe_allow_html=True)

# -----------------------------
# Sales by Region
# -----------------------------

region_sales = (
    filtered_df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)
fig_region = px.bar(
    region_sales,
    x="Sales",
    y="Region",
    orientation="h",
    color="Sales",
    color_continuous_scale="Blues",
    text_auto=".2s"
)

fig_region.update_traces(
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Sales: <b>$%{x:,.0f}</b><extra></extra>"
)

premium_chart(
    fig_region,
    f"🌍 Sales by Region ({selected_region})"
)

# -----------------------------
# Top 5 States
# -----------------------------

top_states = (
    filtered_df
    .groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

fig_states = px.bar(
    top_states,
    x="Sales",
    y="State",
    orientation="h",
    color="Sales",
    color_continuous_scale="Turbo",
    text_auto=".2s"
)

fig_states.update_traces(
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Sales: <b>$%{x:,.0f}</b><extra></extra>"
)

premium_chart(
    fig_states,
    f"🏙️ Top 5 States ({selected_region})"
)

fig_states.update_layout(
    xaxis_title="Sales",
    yaxis_title="",
    yaxis=dict(categoryorder="total ascending")
)

# -----------------------------
# Top 5 Products
# -----------------------------

top_products = (
    filtered_df
    .groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)

# Shorten long product names
top_products["Product Name"] = (
    top_products["Product Name"]
    .str.slice(0, 28) + "..."
)

fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Sales",
    color_continuous_scale="Purples",
    text_auto=".2s"
)

fig_products.update_traces(
    textposition="outside",
    hovertemplate="<b>%{y}</b><br>Sales: <b>$%{x:,.0f}</b><extra></extra>"
)

premium_chart(
    fig_products,
    f"🏆 Top 5 Products ({selected_region})"
)

fig_products.update_layout(
    xaxis_title="Sales",
    yaxis_title="",
    yaxis=dict(categoryorder="total ascending")
)

with row1:
    st.plotly_chart(fig_region, use_container_width=True)

with row2:
    st.plotly_chart(fig_states, width="stretch")

with row3:
    st.plotly_chart(fig_products, width="stretch")
st.markdown("</div>", unsafe_allow_html=True)
# ============================================
# DATA SECTION
# ============================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#111827;
padding:18px;
border-radius:18px;
margin-top:10px;
margin-bottom:15px;
border-left:6px solid #7C3AED;
">

<h2 style="
color:white;
margin:0;
">
📋 Business Records
</h2>

<p style="
color:#94A3B8;
margin-top:8px;
">
Filtered sales transactions available for download.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:#111827;
padding:15px;
border-radius:18px;
border:1px solid rgba(255,255,255,.08);
margin-bottom:15px;
">
""", unsafe_allow_html=True)

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=400,
    hide_index=True
)
st.markdown("</div>", unsafe_allow_html=True)

# ============================================
# DOWNLOAD BUTTON
# ============================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

col1, col2, col3 = st.columns([1,1,3])

with col1:

    st.download_button(

        "📥 Download CSV",

        data=csv,

        file_name="Business_Insights.csv",

        mime="text/csv"

    )

with col2:

    st.button("🔄 Refresh Dashboard")

# ============================================
# FOOTER
# ============================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""

<hr style="border:1px solid #334155;">

<center>

<h4 style="color:white;">
📊 Business Insights Dashboard
</h4>

<p style="color:#94A3B8;">

Developed using

<b>Python</b> •
<b>Streamlit</b> •
<b>Pandas</b> •
<b>Plotly</b>

</p>

<p style="color:#64748B;">

Interactive Business Intelligence Dashboard

</p>

</center>

""", unsafe_allow_html=True)