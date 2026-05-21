using Microsoft.EntityFrameworkCore;
using IdentityManager.Models;

namespace IdentityManager.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<UserIdentity> Identities => Set<UserIdentity>();
    public DbSet<Role> Roles => Set<Role>();
    public DbSet<Entitlement> Entitlements => Set<Entitlement>();
    public DbSet<AccessRequest> AccessRequests => Set<AccessRequest>();
    public DbSet<Connector> Connectors => Set<Connector>();
    public DbSet<Application> Applications => Set<Application>();
    public DbSet<WorkflowStep> WorkflowSteps => Set<WorkflowStep>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        modelBuilder.Entity<UserIdentity>()
            .HasMany(u => u.Roles)
            .WithMany();

        modelBuilder.Entity<Role>()
            .HasMany(r => r.Entitlements)
            .WithMany();

        modelBuilder.Entity<Application>()
            .HasMany(a => a.Entitlements)
            .WithMany();
    }
}
