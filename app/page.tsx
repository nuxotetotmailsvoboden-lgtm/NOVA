import Layout from "@/components/Layout";

import Hero from "@/components/Hero";

import Services from "@/components/sections/Services";
import Portfolio from "@/components/sections/Portfolio";
import Calculator from "@/components/sections/Calculator";
import Showcase from "@/components/showcase/Showcase";
import Reviews from "@/components/sections/Reviews";
import FAQ from "@/components/sections/FAQ";
import CTA from "@/components/sections/CTA";
import Contact from "@/components/sections/Contact";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <Layout>

      <Hero />

      <Services />

      <Portfolio />

      <Calculator />

      <Showcase />

      <Reviews />

      <FAQ />

      <CTA />

      <Contact />

      <Footer />

    </Layout>
  );
}
