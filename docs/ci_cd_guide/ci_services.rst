*******************
CI Services Overview
*******************

NumFOCUS has experience with several CI/CD service providers. This section describes the different types of services available and highlights some specific options.

Types of CI Services
====================

**Platform as a Service (PaaS)**
   Managed services where you write CI configuration but don't manage infrastructure
   
   - **Pros:** Easy to use, minimal maintenance, integrated with repositories
   - **Cons:** Less customization, may have resource limits
   - **Examples:** GitHub Actions, GitLab CI, CircleCI

**Infrastructure as a Service (IaaS)**
   Rent compute resources and manage your own CI infrastructure
   
   - **Pros:** Highly customizable, fine-grained control, can optimize costs
   - **Cons:** More complex to set up and maintain, need DevOps expertise
   - **Examples:** AWS, Google Cloud Platform, Azure

**Specialty Services**
   Services optimized for specific hardware or use cases
   
   - **Pros:** Excellent for niche needs, good vendor support
   - **Cons:** Fewer built-in integrations, smaller communities
   - **Examples:** CirrusCI, UbiCloud

Recommended Services
===================

**GitHub Actions**
   GitHub's native CI/CD platform
   
   - **Best for:** Projects already on GitHub
   - **Pricing:** Free tier generous; paid tier very competitive
   - **Hardware:** Standard Linux, macOS, Windows; some GPU support
   - **Pros:** 
      - Integrated directly with GitHub
      - Actions Marketplace with reusable workflows
      - Self-hosted runners for custom hardware
      - Excellent documentation and large community
   - **Cons:** 
      - Self-hosted runners require maintenance
      - Matrix complexity can be challenging
   - **NumFOCUS experience:** Widely used by NumFOCUS projects

**CirrusCI**
   Optimized for open source with free credits
   
   - **Best for:** Projects needing exotic hardware or cross-platform testing
   - **Pricing:** Free credits for open source; pay-as-you-go for overage
   - **Hardware:** Excellent exotic hardware support (ARM, etc.); custom pools available
   - **Pros:** 
      - Built-in open source credits
      - Excellent for non-standard architectures
      - Good vendor support
      - Flexible configuration
   - **Cons:** 
      - Smaller community than GitHub Actions
      - Learning curve for Starlark configuration
   - **NumFOCUS experience:** Used by NumPy, MDAnalysis, and other projects

**UbiCloud**
   GitHub Actions-compatible with custom offerings
   
   - **Best for:** Projects wanting GitHub Actions compatibility with custom hardware
   - **Pricing:** Competitive; willing to work with NumFOCUS on terms
   - **Hardware:** Full GitHub Actions compatibility; custom bare metal options
   - **Pros:** 
      - Drop-in GitHub Actions replacement
      - Willing to customize for open source projects
      - Competitive pricing for large workloads
      - Open to bulk agreements
   - **Cons:** 
      - Smaller than GitHub or CircleCI
      - Less community content
   - **NumFOCUS experience:** Growing adoption; good vendor relationship

**AWS/GCP/Azure**
   Cloud providers with CI/CD offerings
   
   - **Best for:** Projects with highly specialized infrastructure needs
   - **Pricing:** Varies widely; can be cost-effective at scale
   - **Hardware:** Access to full cloud portfolio including GPU, specialized hardware
   - **Pros:** 
      - Maximum flexibility and customization
      - Can integrate with other cloud services
      - Competitive volume pricing
   - **Cons:** 
      - Complex setup and maintenance
      - Requires DevOps expertise
      - Can be expensive without careful optimization
   - **NumFOCUS experience:** Some projects use AWS; coordination through NumFOCUS can help with credits

**Self-Hosted Runners**
   Run CI on your own hardware
   
   - **Best for:** Projects with very specific hardware needs or budget constraints
   - **Pricing:** Only hardware costs (electricity, depreciation, labor)
   - **Hardware:** Whatever you want!
   - **Pros:** 
      - No CI service costs
      - Full control over environment
      - Can use specialized hardware
   - **Cons:** 
      - Significant maintenance burden
      - Requires reliable hardware and network
      - Need to manage access and security
      - Complex scaling
   - **NumFOCUS experience:** Used by some projects; generally recommend managed services if possible

Making a Choice
==============

Start by answering these questions:

1. **Are you on GitHub?** → GitHub Actions is likely your best bet
2. **Do you need exotic hardware?** → CirrusCI or UbiCloud
3. **Do you have DevOps resources?** → Consider AWS/GCP/Azure
4. **Do you have existing infrastructure?** → Self-hosted runners
5. **Do you want GitHub Actions compatibility?** → UbiCloud

Next, consider:

- Your testing frequency and duration
- Your hardware requirements (CPU, RAM, GPU, architecture)
- Your budget (get estimates from each vendor)
- Maintenance burden your team can handle
- Community and support options

Don't forget to check if NumFOCUS can help negotiate better terms or provide funding for your choice!

