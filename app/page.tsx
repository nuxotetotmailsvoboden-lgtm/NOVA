import Layout from "@/components/Layout";
import Hero from "@/components/Hero";
import Services from "@/components/sections/Services";
import Portfolio from "@/components/sections/Portfolio";
import Calculator from "@/components/sections/Calculator";

export default function Home() {
  return (
    <Layout>
      <Hero />
      <Services />
      <Portfolio />
      <Calculator />
    </Layout>
  );
}
