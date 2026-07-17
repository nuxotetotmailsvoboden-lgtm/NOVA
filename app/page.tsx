import Layout from "@/components/Layout";
import Hero from "@/components/Hero";
import Services from "@/components/sections/Services";
import Portfolio from "@/components/sections/Portfolio";

export default function Home() {
  return (
    <Layout>
      <Hero />
      <Services />
      <Portfolio />
    </Layout>
  );
}
